import asyncio
from aogram import Bot, Dispatcher, types
from aogram.filters import Command

BOT_TOKEN = "8790497773:AAEIBY8sKUaPKXMedX9h-baPS9mPv5Qwpmw"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Хранилище состояний
states = {}

@dp.message()
async def auto_reply(message: types.Message):
    chat_id = str(message.chat.id)
    if states.get(chat_id, True):
        await message.reply(
            "Владелец не в сети, пожалуйста, подождите, пока ответит 😊"
        )

@dp.message(Command("on"))
async def turn_on(message: types.Message):
    chat_id = str(message.chat.id)
    states[chat_id] = True
    await message.reply("✅ Автоответ включён")

@dp.message(Command("off"))
async def turn_off(message: types.Message):
    chat_id = str(message.chat.id)
    states[chat_id] = False
    await message.reply("❌ Автоответ выключен")

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.reply(
        "👋 Привет! Я автоответчик.\n\n"
        "/on — включить автоответ\n"
        "/off — выключить автоответ"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
