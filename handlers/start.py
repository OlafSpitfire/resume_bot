from aiogram import types
from aiogram.types import InputFile

from loadings import dp, bot

from texts.start_text import start_text
from texts.start_text_ukr import start_text_ukr
from keyboards.inline.start_keyb import start_keyb, start_keyb_ukr
from keyboards.inline.language_selection import language_selection

from middlewares.Throttling import rate_limit
from middlewares.Inline_Throttling import rate_limit_inline


@rate_limit()
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    photo = InputFile(path_or_bytesio="media/IMG_20230203_142358.jpg")
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer("Choice of resume language", reply_markup=language_selection)


@rate_limit_inline()
@dp.callback_query_handler(lambda call: call.data.startswith("lang"))
async def select_languague(callback: types.CallbackQuery):
    if callback.data == "lang_ukr":
        await callback.message.edit_text(text=start_text_ukr, reply_markup=start_keyb_ukr)
    elif callback.data == "lang_eng":
        await callback.message.edit_text(text=start_text, reply_markup=start_keyb)
