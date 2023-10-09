import threading
from aiogram import types
import easyocr
from main import bot, token
from functions.private_functions.gpt import *
import asyncio

async def textr(file_path, content):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, lambda: process_text(file_path, content))
    return result

def process_text(file_path, content):
    print('in process 2')
    reader =  easyocr.Reader(['ru', 'en'])
    result =  reader.readtext(file_path, detail=0)
    text =''
    for results in result:
        text=str(text)+' '+str(results)
    print(text)
    text =  asyncio.run(generate_completion(text, content=content))
    return text

async def getphoto(photo, content):
    print('in process')
    photo_id = photo.file_id
    photo_obj = await bot.get_file(photo_id)
    photo_path = photo_obj.file_path
    file_url = f'https://api.telegram.org/file/bot{token}/{photo_path}'

    # Вызываем textr асинхронно
    text = await textr(file_url, content)
    print(text)

    return text
