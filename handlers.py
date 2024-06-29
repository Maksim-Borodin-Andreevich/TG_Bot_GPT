from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import kb
import text

router = Router()


@router.message(CommandStart())
async def start_hendler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.first_name), reply_markup=kb.price)
    
@router.message(Command('price'))
async def start_hendler(msg: Message):
    await msg.answer(text.price.format(name=msg.from_user.first_name), reply_markup=kb.price)
    
@router.message(F.text == 'стоимость')
async def menu(msg: Message):
    await msg.answer(text.price, reply_markup=kb.price)

@router.callback_query(F.data == 'help')
async def help_user(call: CallbackQuery):
    await call.message.answer(text.support)