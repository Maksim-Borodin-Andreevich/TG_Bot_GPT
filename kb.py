from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


price=[
    [
    InlineKeyboardButton(text="💳 Купить 75 vp", callback_data="buy_75"),
    InlineKeyboardButton(text="💳 Купить 1000 vp", callback_data="buy_1000"),
     
    
    InlineKeyboardButton(text="💳 Купить 95959 vp", callback_data="buy_95959"),
    ],
    
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]

]

price = InlineKeyboardMarkup(inline_keyboard=price)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='◀️ Выйти в меню')]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='◀️ Выйти в меню', callback_data='menu')]])
