#!/usr/bin/env python3

import subprocess
import asyncio
from telegram import Bot

from time import sleep

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
