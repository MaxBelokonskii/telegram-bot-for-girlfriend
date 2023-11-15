import requests
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, KeyboardButton, ReplyKeyboardMarkup
import aiohttp
import os
from environs import Env


env = Env()
env.read_env()

API_DOG_URL = 'https://random.dog/woof.json'
BOT_TOKEN = env('BOT_TOKEN')


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


dog_response: requests.Response
cat_link: str
chat_id: int

btn_1 = KeyboardButton(text='Я устала')
btn_2 = KeyboardButton(text='Мне грустно')
btn_3 = KeyboardButton(text='Мне одиноко')
btn_4 = KeyboardButton(text='Скажи, что ты меня любишь')
btn_5 = KeyboardButton(text='Скажи, что ты по мне скучаешь')
btn_6 = KeyboardButton(text='Хочу собаку!')
keyboard = ReplyKeyboardMarkup(keyboard=[[btn_1, btn_2, btn_3],[btn_4, btn_5], [btn_6]], resize_keyboard=True)

#Команда /start
async def process_start_command(message: Message):
  await message.answer('Малышик, Привет!\nЭтого бота я сделал специально для тебя!\nОн сделан для того, чтоб ты могла услышать слова поддержки даже тогда, когда я не могу говорить. Просто выбери нужную кнопку и все увидишь)', reply_markup=keyboard)

#Команда /tired
async def process_tired_command(message: Message):
  voice_file = FSInputFile('tired.ogg')
  await message.answer_voice(voice=voice_file)


#Команда /upset
async def process_upset_command(message: Message):
  voice_file = FSInputFile('upset.ogg')
  await message.answer_voice(voice=voice_file)

#Команда /lonely
async def process_lonely_command(message: Message):
  voice_file = FSInputFile('lonely.ogg')
  await message.answer_voice(voice=voice_file)

#Команда /love
async def process_love_command(message: Message):
  voice_file = FSInputFile('love.ogg')
  await message.answer_voice(voice=voice_file)

#Команда /miss
async def process_miss_command(message: Message):
  voice_file = FSInputFile('miss.ogg')
  await message.answer_voice(voice=voice_file)

#Команда /dog
async def send_dog(message: Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(API_DOG_URL) as response:
            if response.status == 200:
                data = await response.json()
                dog_link = data['url']
                await message.answer_photo(photo=dog_link)
            else:
                await message.answer('Упс!')

dp.message.register(process_start_command, Command(commands=["start"]))
dp.message.register(process_tired_command, Command(commands=["tired"]))
dp.message.register(process_tired_command, F.text == 'Я устала')
dp.message.register(process_upset_command, Command(commands=["upset"]))
dp.message.register(process_upset_command, F.text == 'Мне грустно')
dp.message.register(process_lonely_command, Command(commands=["lonely"]))
dp.message.register(process_lonely_command, F.text == 'Мне одиноко')
dp.message.register(process_love_command, Command(commands=["love"]))
dp.message.register(process_love_command, F.text == 'Скажи, что ты меня любишь')
dp.message.register(process_miss_command, Command(commands=["miss"]))
dp.message.register(process_miss_command, F.text == 'Скажи, что ты по мне скучаешь')
dp.message.register(send_dog, Command(commands=["dog"]))
dp.message.register(send_dog, F.text == 'Хочу собаку!')

if __name__ == '__main__':
  dp.run_polling(bot)