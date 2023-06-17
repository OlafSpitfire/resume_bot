from aiogram import Dispatcher, Bot
from data import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot=bot, storage=storage)
