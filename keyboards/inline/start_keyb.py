from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


start_keyb = InlineKeyboardMarkup(row_width=2)
contacts = InlineKeyboardButton(text="Contacts ☎️", callback_data="E_contacts")
about_me = InlineKeyboardButton(text="About me 👨", callback_data="E_about_me")
experience = InlineKeyboardButton(text="Experience 🧑‍💻", callback_data="E_experience")
skills = InlineKeyboardButton(text="Skills 💪", callback_data="E_skills")
education = InlineKeyboardButton(text="Education 🧑‍🎓", callback_data="E_education")
languages = InlineKeyboardButton(text="Languages 🧑‍🏫", callback_data="E_languages")
start_keyb.row(contacts, about_me).row(experience, skills).row(education, languages)


start_keyb_ukr = InlineKeyboardMarkup(row_width=2)
contacts_ukr = InlineKeyboardButton(text="Контакти ☎️", callback_data="U_contacts")
about_me_ukr = InlineKeyboardButton(text="Про мене 👨", callback_data="U_about_me")
experience_ukr = InlineKeyboardButton(text="Досвід 🧑‍💻", callback_data="U_experience")
skills_ukr = InlineKeyboardButton(text="Навички 💪", callback_data="U_skills")
education_ukr = InlineKeyboardButton(text="Освiта 🧑‍🎓", callback_data="U_education")
languages_ukr = InlineKeyboardButton(text="Мовы 🧑‍🏫", callback_data="U_languages")
start_keyb_ukr.row(contacts_ukr, about_me_ukr).row(experience_ukr, skills_ukr).row(education_ukr, languages_ukr)
