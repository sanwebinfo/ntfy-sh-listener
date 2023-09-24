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