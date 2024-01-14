#!/usr/bin/env python3

"""
Author: Vadim Belous
Email: fancybear@internet.ru 

The main goal of this script is to send notifications to the chat
about the amount of free disk space where this script is running

Dependencies:
pip install psutil python-telegram-bot

Example Usage:
python space_alert.py

Cron job example:
0 * * * * python3 /root/space_alert.py
"""

import asyncio
import psutil
import subprocess
from telegram import Bot



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

async def check_disk_space():
    disk = psutil.disk_usage('/')

    threshold = 10 * 1024 * 1024 * 1024  # 10 gb
    
    df_output = subprocess.check_output(['df', '-h']).decode('utf-8')
    
    if disk.free < threshold:
        message = f"⚠️ Attention! Free space on the server is less than 10 GB. " \
                  f"Currently available: {disk.free / (1024 ** 3):.2f} GB\n\n" \
                  f"Disk usage:\n```\n{df_output}\n```"
        
        await send_alert(message)

    else:   
        message = f"ℹ️ INFO. " \
                  f"Available: {disk.free / (1024 ** 3):.2f} GB\n\n" \
                  f"Disk usage:\n```\n{df_output}\n```"

        await send_alert(message)


async def send_alert(message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")

if __name__ == "__main__":
    asyncio.run(check_disk_space())
