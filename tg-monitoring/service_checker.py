#!/usr/bin/env python3


"""
Author: Vadim Belous
Email: fancybear@internet.ru 

The main goal of this script is to send notifications to the chat
when necessary service/services is/are down on the machine where this script is running

Dependencies:
pip install python-telegram-bot

Example Usage:
python service_checker.py

Systemd service example:

"""

import subprocess
import asyncio
from telegram import Bot

from time import sleep

"""
1. Go to the BotFather and create bot. U will receive a token to access to the http api. Paste ur token to BOT_TOKEN
2. Go to https://api.telegram.org/botX/getUpdates when X - is ur token. U will see chat id. Paste this value to the CHAT_ID

For example, send message via curl:
curl -X POST "https://api.telegram.org/botX/sendMessage" -d "chat_id=Y&text=Z"
When:
    X - Token
    Y - Chat id
    Z - Message

"""

BOT_TOKEN = ''
CHAT_ID = ''


async def send_telegram_message(message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='Markdown')



def check_status(service_name):
    result = subprocess.run(['sudo', 'systemctl', 'is-active', service_name], stdout=subprocess.PIPE)
    status = result.stdout.decode().strip()
    status_emoji = '✅' if status == 'active' else '❌'

    if status != 'active':
        message = f"Status of {service_name}: {status_emoji} {status.capitalize()}"

        loop = asyncio.get_event_loop()
        loop.run_until_complete(send_telegram_message(message))


if __name__ == '__main__':
    while True:
        sleep(5)
        check_status('YOUR SERVICE')
