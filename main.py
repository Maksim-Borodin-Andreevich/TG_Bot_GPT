import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode # содержит настройки разметки сообщений (HTML, Markdown)
from aiogram.fsm.storage.memory import MemoryStorage # Хранилища данных для состояний пользователей

import config
from handlers import router


async def main():
    bot = Bot(token=config.BOT_TOKEN)  
    dp = Dispatcher(storage=MemoryStorage()) # параметр storage=MemoryStorage() говорит о том, что все 
    # данные бота, которые мы не сохраняем в БД (к примеру состояния), будут стёрты при перезапуске
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())