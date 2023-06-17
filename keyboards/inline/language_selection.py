from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


language_selection = InlineKeyboardMarkup(row_width=2)
ukr = InlineKeyboardButton(text="Українська 🇺🇦", callback_data="lang_ukr")
eng = InlineKeyboardButton(text="English 🇬🇧", callback_data="lang_eng")
language_selection.row(ukr, eng)
