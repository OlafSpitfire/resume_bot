from aiogram import types
from loadings import dp, bot

from texts.resume.contacts import contacts, contacts_ukr
from texts.resume.about_me import about_me, about_me_ukr
from texts.resume.experience import experience, experience_ukr
from texts.resume.skills import skills, skills_ukr
from texts.resume.education import education, education_ukr
from texts.resume.languagues import languagues, languagues_ukr

from keyboards.inline.del_some_msg import del_some_msg

from middlewares.Inline_Throttling import rate_limit_inline


@rate_limit_inline()
@dp.callback_query_handler(lambda call: call.data.startswith('E_'))
async def my_resume_data(callback: types.CallbackQuery):
    if callback.data == "E_contacts":
        await bot.send_message(chat_id=callback.message.chat.id, text=contacts,
                               parse_mode="HTML", reply_markup=del_some_msg)
        await callback.answer()
    elif callback.data == "E_about_me":
        await bot.send_message(chat_id=callback.message.chat.id, text=about_me, reply_markup=del_some_msg)
        await callback.answer()
    elif callback.data == "E_experience":
        await bot.send_message(chat_id=callback.message.chat.id, text=experience, reply_markup=del_some_msg)
        await callback.answer()
    elif callback.data == "E_skills":
        await bot.send_message(chat_id=callback.message.chat.id, text=skills, reply_markup=del_some_msg)
        await callback.answer()
    elif callback.data == "E_education":
        await bot.send_message(chat_id=callback.message.chat.id, text=education, reply_markup=del_some_msg)
        await callback.answer()
    elif callback.data == "E_languages":
        await bot.send_message(chat_id=callback.message.chat.id, text=languagues, reply_markup=del_some_msg)
        await callback.answer()


@rate_limit_inline()
@dp.callback_query_handler(lambda call: call.data.startswith('U_'))
async def my_resume_data(callback: types.CallbackQuery):
    if callback.data == "U_contacts":
        await bot.send_message(chat_id=callback.message.chat.id, text=contacts_ukr,
                               parse_mode="HTML", reply_markup=del_some_msg)
        await callback.answer()
    elif callback.data == "U_about_me":
        await bot.send_message(chat_id=callback.message.chat.id, text=about_me_ukr, reply_markup=del_some_msg)
        await callback.answer()
    elif callback.data == "U_experience":
        await bot.send_message(chat_id=callback.message.chat.id, text=experience_ukr, reply_markup=del_some_msg)
        await callback.answer()
    elif callback.data == "U_skills":
        await bot.send_message(chat_id=callback.message.chat.id, text=skills_ukr, reply_markup=del_some_msg)
        await callback.answer()
    elif callback.data == "U_education":
        await bot.send_message(chat_id=callback.message.chat.id, text=education_ukr, reply_markup=del_some_msg)
        await callback.answer()
    elif callback.data == "U_languages":
        await bot.send_message(chat_id=callback.message.chat.id, text=languagues_ukr, reply_markup=del_some_msg)
        await callback.answer()


@dp.callback_query_handler(lambda call: call.data.startswith('del_this_one'))
async def close_this_message(callback: types.CallbackQuery):
    if callback.data == "del_this_one":
        if callback.message:
            await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
