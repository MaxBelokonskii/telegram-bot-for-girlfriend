from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

from environs import Env
from functions import *

env = Env()
env.read_env()

API_DOG_URL = 'https://random.dog/woof.json'
BOT_TOKEN = env('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.message.register(start_command, Command(commands=["start"]))
dp.message.register(tired_command, Command(commands=["tired"]))
dp.message.register(tired_command, F.text == 'Я устала')
dp.message.register(upset_command, Command(commands=["upset"]))
dp.message.register(upset_command, F.text == 'Мне грустно')
dp.message.register(lonely_command, Command(commands=["lonely"]))
dp.message.register(lonely_command, F.text == 'Мне одиноко')
dp.message.register(love_command, Command(commands=["love"]))
dp.message.register(love_command, F.text == 'Скажи, что ты меня любишь')
dp.message.register(miss_command, Command(commands=["miss"]))
dp.message.register(miss_command, F.text == 'Скажи, что ты по мне скучаешь')
dp.message.register(who_command, Command(commands=["who"]))
dp.message.register(who_command, F.text == 'Кто я для тебя?')
dp.message.register(send_dog, Command(commands=["dog"]))
dp.message.register(send_dog, F.text == 'Хочу собаку!')

if __name__ == '__main__':
    dp.run_polling(bot)
