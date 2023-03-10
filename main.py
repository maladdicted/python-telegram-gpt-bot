import openai
from re import sub
from os import environ
from aiogram import Bot, Dispatcher, executor, types

openai.api_key = environ.get("OPENAI_TOKEN")
bot = Bot(token = environ.get("BOT_TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler(commands=["gpt"])
async def send(message : types.Message):
    message_text = sub(r"\s{2,}", " ", message.text.replace("/gpt", "").strip())

    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message_text,
        max_tokens = 1000,
        temperature = 0.6
    )

    await message.reply(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates = True)
