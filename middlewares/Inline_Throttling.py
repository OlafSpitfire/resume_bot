import asyncio

from aiogram import Dispatcher, types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.utils.exceptions import Throttled


def rate_limit_inline(limit: int = 1, key=None):

    def decorator(func):
        setattr(func, 'throttling_rate_limit', limit)
        if key:
            setattr(func, 'throttling_key', key)
        return func

    return decorator


class InlineThrottlingMiddleware(BaseMiddleware):

    def __init__(self, limit: int = 1, key_prefix='antiflood_'):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(InlineThrottlingMiddleware, self).__init__()

    async def on_pre_process_callback_query(self, query: types.CallbackQuery, data: dict):
        handler = current_handler.get()

        dispatcher = Dispatcher.get_current()
        if handler:
            limit = getattr(handler, 'throttling_rate_limit', self.rate_limit)
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_callback"

        try:
            await dispatcher.throttle(key, rate=limit)
        except Throttled as t:
            await self.callback_throttled(query, t)

            raise CancelHandler()

    async def callback_throttled(self, query: types.CallbackQuery, throttled: Throttled):
        handler = current_handler.get()
        if handler:
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")
            delta = throttled.rate - throttled.delta

            if throttled.exceeded_count <= 2:
                await query.answer('Too many')

            await asyncio.sleep(delta)
