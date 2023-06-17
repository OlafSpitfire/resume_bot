from aiogram import Dispatcher

from .Throttling import ThrottlingMiddleware
from .Inline_Throttling import InlineThrottlingMiddleware


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(InlineThrottlingMiddleware())
