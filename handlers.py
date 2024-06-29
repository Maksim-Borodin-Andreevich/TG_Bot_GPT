from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import kb
import text

router = Router()


@router.message(Command('start'))
async def start_hendler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.first_name), reply_markup=kb.price)
    
@router.message(F.text == 'Меню')
@router.message(F.text == 'Выйти в меню')
@router.message(F.text == '◀️ Выйти в меню')
async def menu(msg: Message):
    await msg.answer(text.price, reply_markup=kb.price)

    