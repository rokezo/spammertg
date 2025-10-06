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

    text = """RentBiz 💥  — Надійний партнер покупки / оренди банків.



💸НАШ ПРАЙС:

🏦 PUMB  😎
(18+ років - рег. ) - 1️⃣5️⃣0️⃣0️⃣

🏦 Credit Agricole  😎
(18+ років - рег.) - 7️⃣0️⃣0️⃣

🏦 FreeBank  😎
(18+ років - рег.) - 7️⃣0️⃣0️⃣

🏦 UKRSSIB 2.0  😎
(18+ років - рег.) - 5️⃣0️⃣0️⃣

 🏦Райфайзен 😎
(18+ років - рег.) - 5️⃣0️⃣0️⃣

🏦 Монобанк  😎
(14+ років .) -  1️⃣3️⃣0️⃣0️⃣


📱 ЗВʼЯЗОК: @user2020219 



💳ОПЛАТА ГАРАНТОВАНА ПРОТЯГОМ 1години 💳

🎁БОНУС ЗА ПРИВЕДЕНОГО ДРУГА.

🤝ШУКАЮ ДРОПОВОДІВ!📞

⏰ГРАФІК РОБОТИ:
С 7.00 до 00.00 по Києву — 6/1
Наш канал з відгуками та актуальними цінами: https://t.me/orendam1
 """

    dialogs = await client.get_dialogs()  # Получаем все диалоги

    for dialog in dialogs:
        try:
            # Пропускаем RentBiz
            if dialog.name == "RentBiz":
                print(f"Пропущен: {dialog.name}")
                continue

            # Если обычная группа
            if dialog.is_group:
                await client.send_message(dialog.entity, text)
                print(f"Отправлено в обычную группу: {dialog.name}")
                time.sleep(random.uniform(1, 3))
                continue

            # Если супергруппа (канал, но с megagroup=True)
            if dialog.is_channel and getattr(dialog.entity, "megagroup", False):
                await client.send_message(dialog.entity, text)
                print(f"Отправлено в супергруппу: {dialog.name}")
                time.sleep(random.uniform(1, 3))

        except Exception as e:
            print(f"Ошибка при отправке в {dialog.name}: {e}")
            time.sleep(1)

with client:
    client.loop.run_until_complete(main())
