from os import terminal_size

from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import KeyboardBuilder, ReplyKeyboardBuilder


def main_handler(texts,size):
    rkb =ReplyKeyboardBuilder
    rkb.add(*[KeyboardButton(text=text )for text in texts ])
    rkb.adjust(*size)
    return rkb.as_markup(resize_keyboard=True, one_time_keyboard=True)