import logging
import random
import sqlite3
import datetime
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram import ReplyKeyboardMarkup


BOT_TOKEN = "6316601466:AAGR0OJks7WwNgvbr6gj2uJzHBU47SH0JK0"
reply_keyboard = [['/start', '/help', "/info", "/day"]]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TIMER = 5


async def start(update, context):
    img = open('card.jpg', 'rb')
    await context.bot.send_photo(
        update.message.chat_id,
        img,
        caption="Приветствую в нашем уютном боте! Тут вы узнаете будущее и немножко больше) выберите какой расклад вам нужен:",
        reply_markup=markup
    )


async def help(update, context):
    await update.message.reply_text(
        "Я бот справочник.")


async def info(update, context):
    await update.message.reply_text(
        "Наш бот не идиален, если Вас заинтересовало гадание, то можете узнать подробнее перейдя по ссылке https://gadalkindom.ru/gadanie/taro/znachenie-kart-taro ")


async def day(update, context):
    name_table = ["Wands", "Cup", "Swords", "Pentacles", "Senior"]
    table = random.choice(name_table)
    name_bd = "Taro"
    con = sqlite3.connect(name_bd)
    cur = con.cursor()
    result = cur.execute(
            f"""SELECT name FROM {table}""").fetchall()
    name = list(random.choice(result))
    name = name[0]
    up = random.choice(["linear", "overturn"])
    result = cur.execute(
            f"""SELECT {up}, name FROM {table}
                """).fetchall()
    value = ""
    for el in result:
        if el[1] == name:
            value = el[0]
    con.close()
    img = open('card.jpg', 'rb')
    await context.bot.send_photo(
        update.message.chat_id,
        img,
        caption=value,
        reply_markup=markup
    )


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, start)
    application.add_handler(text_handler)
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("day", day))
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
