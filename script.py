from telethon import TelegramClient

api_id = 26753991
api_hash = '91ed1cdb2cb8b6018d0354106bf11ad9'  
session_name = 'userbot' 

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    me = await client.get_me()
    print("Подключились как:", me.username)

with client:
    client.loop.run_until_complete(main())




from telethon import TelegramClient, errors
import asyncio
import time
import random

api_id = 26753991
api_hash = '91ed1cdb2cb8b6018d0354106bf11ad9'
session_name = 'userbot'

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    me = await client.get_me()
    print("Подключились как:", me.username)

    text = """📢 Орендую ваші карти

💵 ПУМБ — 1500
💵 УкрСиб — 750
💵 Акорд — 500
💵 FreeBank — 500
💵 Альянс (ліміт 50k) — 500
💵 MonoBank 14+ — 800–1000

✨ Є багато відгуків — все можна переглянути в Telegram (біо).

✍️ Писати: @user2020219"""



    dialogs = await client.get_dialogs()  # Получаем все диалоги

    for dialog in dialogs:
        try:
            # Фильтруем: отправляем только пользователям и группам
            if dialog.is_channel or dialog.is_group:
                await client.send_message(dialog.entity, text)
                print(f"Отправлено в: {dialog.name}")
                time.sleep(random.uniform(1, 3))
        except errors.FloodWaitError as e:
            print(f"Нужно подождать {e.seconds} секунд")
            time.sleep(e.seconds + 1)
        except Exception as e:
            print(f"Ошибка при отправке в {dialog.name}: {e}")
            time.sleep(1)

with client:
    client.loop.run_until_complete(main())
