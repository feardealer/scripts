#!/usr/bin/env python3

import asyncio
import psutil
import subprocess
from telegram import Bot

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
