import random
from aiogram.types import Message, FSInputFile
import aiohttp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_DOG_URL = 'https://random.dog/woof.json'

btn_1 = KeyboardButton(text='Я устала')
btn_2 = KeyboardButton(text='Мне грустно')
btn_3 = KeyboardButton(text='Мне одиноко')
btn_4 = KeyboardButton(text='Скажи, что ты меня любишь')
btn_5 = KeyboardButton(text='Скажи, что ты по мне скучаешь')
btn_6 = KeyboardButton(text='Кто я для тебя?')
btn_7 = KeyboardButton(text='Хочу собаку!')
keyboard = ReplyKeyboardMarkup(keyboard=[[btn_1, btn_2, btn_3],[btn_4, btn_5], [btn_6], [btn_7]], resize_keyboard=True)

async def start_command(message: Message):
    await message.answer('Малышик, Привет!\nЭтого бота я сделал специально для тебя!\nОн сделан для того, чтоб ты могла услышать слова поддержки даже тогда, когда я не могу говорить. Просто выбери нужную кнопку и все увидишь)', reply_markup=keyboard)

async def tired_command(message: Message):
    voice_path = random.choice(['./oggs/tired.ogg', './oggs/tired_2.ogg'])
    voice_file = FSInputFile(voice_path)
    await message.answer_voice(voice=voice_file)

async def upset_command(message: Message):
    voice_file = FSInputFile('./oggs/upset.ogg')
    await message.answer_voice(voice=voice_file)

async def lonely_command(message: Message):
    voice_file = FSInputFile('./oggs/lonely.ogg')
    await message.answer_voice(voice=voice_file)

async def love_command(message: Message):
    voice_path = random.choice(['./oggs/love.ogg', './oggs/love_2.ogg'])
    voice_file = FSInputFile(voice_path)
    await message.answer_voice(voice=voice_file)

async def miss_command(message: Message):
    voice_file = FSInputFile('./oggs/miss.ogg')
    await message.answer_voice(voice=voice_file)

async def who_command(message: Message):
    voice_file = FSInputFile('./oggs/whoAmIForYou.ogg')
    await message.answer_voice(voice=voice_file)

async def send_dog(message: Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(API_DOG_URL) as response:
            if response.status == 200:
                data = await response.json()
                dog_link = data['url']
                await message.answer_photo(photo=dog_link)
            else:
                await message.answer('Упс!')
