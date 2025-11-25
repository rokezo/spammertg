from telethon import TelegramClient, errors
import asyncio
import random

api_id = 26753991
api_hash = '91ed1cdb2cb8b6018d0354106bf11ad9'
session_name = 'userbot'

client = TelegramClient(session_name, api_id, api_hash)

text = """RentBiz 💥  — Надійний партнер оренди банків.

Актуально 👑

🏦Моно 18+ 1500грн 
🏦Моно 14+ 1300 грн 
🏦Пумб 18+ 1600
🏦Райф 18+ 500 грн 
🏦Изи банк 18+ 500 грн 
🏦Фри банк 18+ 500 грн 
🏦Аккорд 18+ 500 грн 
🏦TAS2U 18+ 300 грн
🏦Alliance (30к лимит) - 600 грн
🏦Alliance (50к лимит) - 600 грн
🏦Укрсиб 2.0 - 600 грн


ФОП: 👑
 
🏦РАЙФ ФОП 4000
🏦МОНО ФОП 4000
🏦ПУМБ ФОП 4000
🏦СЕНС ФОП 3000
🏦УКР СИБ ФОП 2000

📱 ЗВʼЯЗОК: @user2020219

Наш канал з відгуками та актуальними цінами: https://t.me/orendam1
"""

async def send_to_all():
    dialogs = await client.get_dialogs()

    for dialog in dialogs:
        try:
            # Пропускаем чат RentBiz
            if dialog.name == "RentBiz":
                print(f"Пропущен: {dialog.name}")
                continue

            # Обычная группа
            if dialog.is_group:
                await client.send_message(dialog.entity, text)
                print(f"Отправлено в группу: {dialog.name}")
                await asyncio.sleep(random.uniform(1, 3))
                continue

            # Супергруппа
            if dialog.is_channel and getattr(dialog.entity, "megagroup", False):
                await client.send_message(dialog.entity, text)
                print(f"Отправлено в супергруппу: {dialog.name}")
                await asyncio.sleep(random.uniform(1, 3))

        except Exception as e:
            print(f"Ошибка при отправке в {dialog.name}: {e}")
            await asyncio.sleep(1)

async def main():
    me = await client.get_me()
    print("Подключились как:", me.username)

    while True:
        print("🚀 Начинаем рассылку...")
        await send_to_all()
        print("⏳ Ожидание 10 минут до следующей рассылки...")
        await asyncio.sleep(600)  # 600 сек = 10 минут

with client:
    client.loop.run_until_complete(main())
