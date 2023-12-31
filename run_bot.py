async def on_startup(dp):
    import middlewares
    middlewares.setup(dp)

    from utils.bot_set_commands import set_default_commands
    await set_default_commands(dp)


if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
