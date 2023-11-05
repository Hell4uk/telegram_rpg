from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='⚔️ Битва', callback_data='press_fight'),
        InlineKeyboardButton(text='🪙 Баланс', callback_data='press_balance'),
        InlineKeyboardButton(text='📦 Кейсы', callback_data='press_cases')
     ],
    [
        InlineKeyboardButton(text='✨ Лвл', callback_data='press_lvl'),
        InlineKeyboardButton(text='🗡️ Меч', callback_data='press_sword'),
        InlineKeyboardButton(text='🎫 Статус', callback_data='press_status')
    ]
])

catalog_cases = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='📦 Кейс: Начальный (50🪙)', callback_data='press_case_1'),
        InlineKeyboardButton(text='📦 Кейс: Средний (100🪙)', callback_data='press_case_2')
    ], [
        InlineKeyboardButton(text='📦 Кейс: Профисиональный (500🪙)', callback_data='press_case_3'),
        InlineKeyboardButton(text='📦 Кейс: Премиум (2000🪙) (Premium🎫)', callback_data='press_case_4')
    ]
])