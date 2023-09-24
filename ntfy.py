from dotenv import load_dotenv
import websocket
import json
import os
import requests

load_dotenv()

ntfy_ws = os.environ["NTFY_WS"]
ntfy_topic = os.environ["NTFY_TOPIC"]
telegram_bot = os.environ["TELEGRAM_BOT"]
chat_id = os.environ["TELEGRAM_ID"]

def on_message(ws, message):
    msg = json.loads(message)
    if not 'title' in msg or len(msg['title']) == 0:
       print('\n >>> Ntfy.sh websocket Successfully Passing...! \n')
    else:
        headers = {"content-type": "application/x-www-form-urlencoded"}
        querystring = {"chat_id": chat_id, "text": msg['title'] + "\n\n" +  msg['message']}
        response = requests.request(
                "POST", telegram_bot, headers=headers, params=querystring)
        print("websocket: " + message + "Ntfy: " + response.text)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("\n NTFY websocket Connection closed \n")

def on_open(ws):
    print("\n >> Opened NTFY websocket connection..! \n")

if __name__ == "__main__":
    wsapp = websocket.WebSocketApp("wss://" + str(ntfy_ws) + ntfy_topic + "/ws",
                                   on_open=on_open,
                                   on_message=on_message,
                                   on_error=on_error,
                                   on_close=on_close)
    wsapp.run_forever()