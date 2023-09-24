# NTFY Listener 🚀

[![docker-image](https://github.com/sanwebinfo/ntfy-sh-listener/actions/workflows/docker.yml/badge.svg)](https://github.com/sanwebinfo/ntfy-sh-listenerr/actions/workflows/docker.yml)  

ntfy.sh to `Telegram` forwarder

Forward ntfy.sh Push Messages 🚀 to `Telegram` by using telegram bot and websocket 🛸

using ntfy.sh websocket to Listen the ntfy.sh topic Push Notifications via websocket Connection and Forward it to Telegram via bot.

## API

Ntfy.sh websocket API - <https://docs.ntfy.sh/subscribe/api/?h=websoc#websockets>

## Setup

- Download or Clone the Repo via git

```sh
git clone https://github.com/sanwebinfo/ntfy-sh-listener
cd ntfy-sh-listener

## install packages
pip install -r requirements.txt
touch .env
```

- Env File `.env`
- Replace `ntfy.sh/` with your push server URL

```sh
NTFY_WS = "ntfy.sh/"
NTFY_TOPIC ="<YOUR TOPIC>"
TELEGRAM_BOT = "https://api.telegram.org/bot<YOUR BOT API TOKEN>/sendMessage"
TELEGRAM_ID = "<CHAT ID>"
```

- Test

```sh
python3 ntfy.py
```

## Docker 🐬

Keep Running the Python Script in Docker  

- Update the `.dockerfile` before build - Replace example `ENV` with yours  

```sh
FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN pip3 install requests python-dotenv websocket-client
ENV NTFY_WS = "ntfy.sh/"
ENV NTFY_TOPIC ="<YOUR TOPIC>"
ENV TELEGRAM_BOT = "https://api.telegram.org/bot<YOUR BOT API TOKEN>/sendMessage"
ENV TELEGRAM_ID = "<CHAT ID>"
COPY ntfy.py /usr/bin
CMD ["python3", "/usr/bin/ntfy.py"]
```

```sh

## Build image
docker build . -t="ntfy-sh-listener"

## List the image
docker image ls

## Create and Test Container
docker run -d --name ntfysh ntfy-sh-listener
docker container ps
docker stop (containerID)

## Run the container forever
docker run -d --restart=always --name ntfysh ntfy-sh-listener

## List Hidden container if error exists
docker ps -a

## other commands
docker logs (containerID)
docker stop (containerID)
docker rm (containerid)
docker docker rmi (imageid)
docker image prune
docker builder prune --all -f
docker system prune --all
docker rm $(docker ps -all -q)
docker rmi $(docker image ls -q)
```

## Inspiration

Pushtify (Gotify to Pushover forwarder) - <https://github.com/sebw/pushtify>

## LICENSE

MIT
