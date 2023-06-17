from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


del_some_msg = InlineKeyboardMarkup()
del_this_one = InlineKeyboardButton(text="close/приховати", callback_data="del_this_one")
del_some_msg.add(del_this_one)
