import asyncio
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# 1. ВСТАВЬ СВОЙ ТОКЕН
TOKEN = "8724533859:AAFdkh2rTYJ_34gTyo48v20iho5DDN8I_wA"
# 2. ВСТАВЬ СВОЙ ID (Узнай его у бота @userinfobot)
ADMIN_ID = 6311691133  # Сюда придут чеки от людей

bot = Bot(token=TOKEN)
dp = Dispatcher()

def main_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="📸 Пришли картинку")
    builder.button(text="💳 Поддержать (50 сом)")
    builder.button(text="ℹ️ Информация")
    builder.button(text="🎮 Игра")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Привет! Помоги мне накопить на видеокарту 🎮", reply_markup=main_menu())

# ОБРАБОТКА КНОПКИ ПОДДЕРЖКИ
@dp.message(F.text == "💳 Поддержать (50 сом)")
async def pay_50(message: types.Message):
    # Твои данные MBANK
    my_phone = "0700847284" # Твой номер
    my_name = "Адильхан.К" # Твое имя в банке
    
    text = (
        "<b>💎 Поддержка автора — 50 сом</b>\n\n"
        f"1. Переведи 50 сом на MBANK по номеру: <code>{my_phone}</code>\n"
        f"2. Получатель: <b>{my_name}</b>\n"
        "3. Сделай скриншот чека и пришли его прямо сюда.\n\n"
        "<i>После проверки я добавлю тебя в список VIP-друзей!</i>"
    )
    await message.answer(text, parse_mode="HTML")

# ЛОВИМ ЧЕК (ФОТО)
@dp.message(F.photo)
async def handle_receipt(message: types.Message):
    # Бот подтверждает пользователю
    await message.answer("✅ Чек отправлен автору на проверку! Ожидай подтверждения.")
    
    # Бот пересылает чек ТЕБЕ (админу)
    await bot.send_photo(
        chat_id=ADMIN_ID, 
        photo=message.photo[-1].file_id,
        caption=f"💰 НОВЫЙ ЧЕК!\nОт: @{message.from_user.username}\nID: {message.from_user.id}"
    )

async def main():
    print("Бот запущен! Ждем донаты на видеокарту.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Выключен")
