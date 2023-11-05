import asyncio
from cases import *
from aiogram import Bot, F, types, Dispatcher
from aiogram import Router
from keep_alive import keep
from aiogram.filters import Command
from mkeyboard import main_keyboard, catalog_cases
import asyncio
from database import Sqlite
from aiogram.types.callback_query import CallbackQuery
from fight import *

db = Sqlite('server2.db')


bot = Bot(token='6796889575:AAEzdY7TVbIZZjMkcvV7BScI7C3lL-m2uSU')
dp = Dispatcher()

@dp.message(Command('about'))
async def cmd_about(msg: types.Message):
    await msg.reply('❤️ В разработке бота участвовали:\nПрограммист-директор: @hell4uk\nКонтент-мейкер: @szxtta')

@dp.message(Command('start'))
async def cmd_startbot(msg: types.Message):
    username, id = msg.from_user.username, msg.from_user.id
    await msg.answer(text=f'🖐️ {username}, вот мои команды:\n/case - Открыть кейсы (В ИНВЕНТАРЕ ОСТАЕТСЯ ТОЛЬКО ПОСЛЕДНИЙ ДРОП!)\n/sword - ваш меч\n/about - о нас\n/fight - битва\n/lvl - ваш лвл\n/balance - баланс\n/menu - Кнопочное меню (Рекомендовано!)', reply_markup=main_keyboard)
    db.create_profile(id)

@dp.message(Command('balance'))
async def cmd_balance(msg: types.Message):
    username, id = msg.from_user.username, msg.from_user.id
    await msg.answer(text=f'🪙{username}, ваш баланс: {db.return_coin(id)}')

@dp.message(Command('cases'))
async def cmd_catalog_case(msg: types.Message):
    username, id = msg.from_user.username, msg.from_user.id
    await msg.answer(text=f'{username}, вот все кейсы:', reply_markup=catalog_cases)

@dp.message(Command('sword'))
async def cmd_sword(msg: types.Message):
    username, id = msg.from_user.username, msg.from_user.id
    await msg.answer(text=f'🗡️ {username}, ваше оружие:\n\n {db.return_inv(id)}')

@dp.message(Command('fight'))
async def cmd_fight(msg: types.Message):
    username, id = msg.from_user.username, msg.from_user.id
    await msg.answer(text=sync_fight(id, username, db))

@dp.message(Command('lvl'))
async def cmd_returnlvl(msg: types.Message):
    username, id = msg.from_user.username, msg.from_user.id
    await msg.answer(text=f'✨ {username}, ваш лвл: {db.return_lvl(id)}')
    db.add_coin(id, 100)

@dp.message(Command('menu'))
async def cmd_menu(msg: types.Message):
    username, id = msg.from_user.username, msg.from_user.id
    await msg.answer(text=f'✨ {username}, вот меню: ', reply_markup=main_keyboard)


@dp.callback_query(F.data == 'press_sword')
async def cb_sword(callback: types.CallbackQuery):
    username, id = callback.from_user.username, callback.from_user.id
    await callback.message.answer(text=f'🗡️ {username}, ваше оружие:\n\n {db.return_inv(id)}', reply_markup=main_keyboard)
    await callback.answer()

@dp.callback_query(F.data == 'press_fight')
async def cb_fight(callback: types.CallbackQuery):
    username, id = callback.from_user.username, callback.from_user.id
    await callback.message.answer(text=sync_fight(id, username, db), reply_markup=main_keyboard)
    await callback.answer()

@dp.callback_query(F.data == 'press_balance')
async def cb_balance(callback: types.CallbackQuery):
    username, id = callback.from_user.username, callback.from_user.id
    await callback.message.answer(text=f'🪙{username}, ваш баланс: {db.return_coin(id)}', reply_markup=main_keyboard)
    await callback.answer()

@dp.callback_query(F.data == 'press_lvl')
async def cb_lvl(callback: types.CallbackQuery):
    username, id = callback.from_user.username, callback.from_user.id
    await callback.message.answer(text=f'✨ {username}, ваш лвл: {db.return_lvl(id)}')
    db.add_coin(id, 100)
    await callback.answer()

@dp.callback_query(F.data == 'press_cases')
async def cb_cases_ctg(callback: types.CallbackQuery):
    username, id = callback.from_user.username, callback.from_user.id
    await callback.message.answer(text=f'{username}, вот все кейсы:', reply_markup=catalog_cases)

@dp.callback_query(F.data == 'press_case_1')
async def cb_case1(callback: types.CallbackQuery):
    username, id = callback.from_user.username, callback.from_user.id
    if db.return_coin(id) >= 50:
        db.minus_coin(id, 50)
        drop = sync_open_case(id, weights=[0.8, 0.1, 0.08, 0.02, 0], chance=0.1)
        db.clear_inventory(id)
        await callback.message.answer(text=f'📦 {username}, вы открыли: Начальный кейс, вам выпало: {drop}', reply_markup=catalog_cases)
        db.add_inv(id, drop)
    else:
        await callback.message.answer(text=f'‼️ {username}, недостаточно средст на балансе!', reply_markup=catalog_cases)
    await callback.answer()

@dp.callback_query(F.data == 'press_case_2')
async def cb_case2(callback: types.CallbackQuery):
    username, id = callback.from_user.username, callback.from_user.id
    if db.return_coin(id) >= 100:
        db.minus_coin(id, 100)
        drop = sync_open_case(id, weights=[0.5, 0.3, 0.15, 0.05, 0], chance=0.1)
        db.clear_inventory(id)
        await callback.message.answer(text=f'📦 {username}, вы открыли: Средний кейс, вам выпало: {drop}', reply_markup=catalog_cases)
        db.add_inv(id, drop)
    else:
        await callback.message.answer(text=f'‼️ {username}, недостаточно средст на балансе!', reply_markup=catalog_cases)
    await callback.answer()

@dp.callback_query(F.data == 'press_case_3')
async def cb_case3(callback: types.CallbackQuery):
    username, id = callback.from_user.username, callback.from_user.id
    if db.return_coin(id) >= 500:
        db.minus_coin(id, 500)
        drop = sync_open_case(id, weights=[0.3, 0.3, 0.3, 0.09999, 0.00001], chance=0.25)
        db.clear_inventory(id)
        await callback.message.answer(text=f'📦 {username}, вы открыли: Профисиональный кейс, вам выпало: {drop}', reply_markup=catalog_cases)
        db.add_inv(id, drop)
    else:
        await callback.message.answer(text=f'‼️ {username}, недостаточно средст на балансе!', reply_markup=catalog_cases)
    await callback.answer()

@dp.callback_query(F.data == 'press_case_4')
async def cb_case4(callback: types.CallbackQuery):
    username, id = callback.from_user.username, callback.from_user.id
    if db.return_status(id) == '🎫Премиум':
        if db.return_coin(id) >= 2000:
            db.minus_coin(id, 2000)
            drop = sync_open_case(id, weights=[0, 0.2, 0.4, 0.39, 0.01], chance=0.6)
            db.clear_inventory(id)
            await callback.message.answer(text=f'📦 {username}, вы открыли: Премиум кейс, вам выпало: {drop}', reply_markup=catalog_cases)
            db.add_inv(id, drop)
        else:
            await callback.message.answer(text=f'‼️ {username}, недостаточно средст на балансе!', reply_markup=catalog_cases)
    else:
        await callback.message.answer(text=f'‼️ {username}, вы не имеете подписку Premium!', reply_markup=catalog_cases)
    await callback.answer()

@dp.callback_query(F.data == 'press_status')
async def cb_status(callback: types.CallbackQuery):
    username, id = callback.from_user.username, callback.from_user.id
    await callback.message.answer(text=f'🎫 {username}, ваш статус: {db.return_status(id)}')

async def main():
    print('Bot is working!!!')
    keep()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())