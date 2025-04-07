import asyncio
import logging
import sys
from os import getenv

import dp
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.buttons.reply import main_handler
from bot.dispatcher import dp


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    texts = ["🟢 Restaurant Menu", "📞 Connect with us","🇬🇧🇺🇿🇸🇮 Languages"]
    markup = main_handler(texts,(2,1))
    await message.answer("Welcome to our Restaurant", reply_markup=markup)

