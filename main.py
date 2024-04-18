import logging
import random
import sqlite3
import aiohttp
import datetime
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup


BOT_TOKEN = "6316601466:AAGR0OJks7WwNgvbr6gj2uJzHBU47SH0JK0"

reply_keyboard = [['/start', '/help', "/info"]]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def zero():
    reply_keyboard = [['/day', '/love', "/where_love"],
                      ['/money', '/future', '/zz'],
                      ['/color']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    reply_keyboard = [['/start', '/help', "/info"]]


async def start(update, context):
    reply_keyboard = [['/day', '/love', "/where_love"],
                      ['/money', '/future', '/zz'],
                      ['/color']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    img = open('card.jpg', 'rb')
    await context.bot.send_photo(
        update.message.chat_id,
        img,
        caption="Приветствую в нашем уютном боте! Тут вы узнаете будущее и немножко больше) выберите какой расклад вам нужен:",
        reply_markup=markup
    )


async def help(update, context):
    await update.message.reply_text(
        f"Привет! Я готова тебе помочь с любым возникшим вопросом. Вот что я умею: \n"
        "1. /start - запускает бота-таролога, \n"
        "2. /help - выводит список доступных команд, \n"
        "3. /info - выводит дополнительную информацию о боте-тарологе и дополнительную информацию о гаданиях и значениях карт \n")


async def info(update, context):
    await update.message.reply_text(
        "Наш бот не идиален, если Вас заинтересовало гадание, то можете узнать подробнее перейдя по ссылке: https://astrohelper.ru/gadaniya/taro/znachenie/ ")


async def day(update, context):
    reply_keyboard = [['/start', '/help', "/info"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

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
    value = name
    for el in result:
        if el[1] == name:
            value += el[0]
    con.close()
    img = open('card.jpg', 'rb')
    await context.bot.send_photo(
        update.message.chat_id,
        img,
        caption=value,
        reply_markup=markup
    )


async def future(update, context):
    reply_keyboard = [['/start', '/help', "/info"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    name_card = []
    for i in range(3):
        name_table = ["Wands", "Cup", "Swords", "Pentacles", "Senior"]
        table = random.choice(name_table)
        name_bd = "Taro"
        con = sqlite3.connect(name_bd)
        cur = con.cursor()

        result = cur.execute(
                f"""SELECT name FROM {table}""").fetchall()
        name = list(random.choice(result))
        name = name[0]
        while name in name_card:
            name = list(random.choice(result))
            name = name[0]
        name_card.append(name)

        up = random.choice(["linear", "overturn"])
        result = cur.execute(
                f"""SELECT {up}, name FROM {table}
                    """).fetchall()
        value = name
        for el in result:
            if el[1] == name:
                value += el[0]
        con.close()

        img = open('card.jpg', 'rb')
        await context.bot.send_photo(
            update.message.chat_id,
            img,
            caption=value,
            reply_markup=markup
        )


async def love(update, context):
    reply_keyboard = [['/start', '/help', "/info"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    name_card = []
    for i in range(5):
        name_table = ["Wands", "Cup", "Swords", "Pentacles", "Senior"]
        table = random.choice(name_table)
        name_bd = "Taro"
        con = sqlite3.connect(name_bd)
        cur = con.cursor()

        result = cur.execute(
                f"""SELECT name FROM {table}""").fetchall()
        name = list(random.choice(result))
        name = name[0]
        while name in name_card:
            name = list(random.choice(result))
            name = name[0]
        name_card.append(name)

        up = random.choice(["linear", "overturn"])
        result = cur.execute(
                f"""SELECT {up}, name FROM {table}
                    """).fetchall()
        value = name
        for el in result:
            if el[1] == name:
                value += el[0]
        con.close()

        img = open('card.jpg', 'rb')
        await context.bot.send_photo(
            update.message.chat_id,
            img,
            caption=value,
            reply_markup=markup
        )
    await update.message.reply_text(
                                    "Любить себя нужно сильнее кого либо <3")


async def where_love(update, context):
    reply_keyboard = [['/start', '/help', "/info"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    geocoder_uri = "http://geocode-maps.yandex.ru/1.x/"
    response = await get_response(geocoder_uri, params={
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "format": "json",
        "geocode": update.message.text
    })

    toponym = response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]

    toponym_coodrinates = toponym["Point"]["pos"]

    toponym_longitude, toponym_lattitude = str(random.uniform(-180, 180)), str(random.uniform(-90, 90))

    delta = "10"

    map_params = {
      "ll": ",".join([toponym_longitude, toponym_lattitude]),
      "spn": ",".join([delta, delta]),
       "l": "map"
    }

    static_api_request = f"http://static-maps.yandex.ru/1.x/?ll={map_params['ll']}&spn={map_params['spn']}&l={map_params['l']}"
    await context.bot.send_photo(
        update.message.chat_id,
        static_api_request,
        caption="Нашёл:",
        reply_markup=markup
    )


async def get_response(url, params):
    logger.info(f"getting {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            return await resp.json()


async def money(update, context):
    reply_keyboard = [['/start', '/help', "/info"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

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
    value = name
    for el in result:
        if el[1] == name:
            value += el[0]
    con.close()
    img = open('card.jpg', 'rb')
    await context.bot.send_photo(
        update.message.chat_id,
        img,
        caption=value,
        reply_markup=markup
    )


men = {
        "овен": 0,
        "телец": 1,
        "близнецы": 2,
        "рак": 3,
        "лев": 4,
        "дева": 5,
        "весы": 6,
        "скорпион": 7,
        "стрелец": 8,
        "козерог": 9,
        "водолей": 10,
        "рыбы": 11
    }

women = {
        "овен": [45, 73, 46, 47, 59, 48, 66, 59, 67, 43, 89, 43],
        "телец": [85, 89, 72, 79, 54, 76, 67, 89, 79, 79, 63, 91],
        "близнецы": [51, 63, 75, 57, 48, 56, 73, 60, 66, 86, 89, 38],
        "рак": [48, 92, 67, 51, 95, 87, 74, 79, 55, 56, 71, 73],
        "лев": [49, 53, 43, 94, 45, 68, 69, 76, 88, 79, 68, 43],
        "дева": [39, 55, 54, 90, 76, 62, 62, 78, 78, 58, 38, 53],
        "весы": [58, 56, 66, 74, 89, 61, 69, 64, 87, 49, 90, 55],
        "скорпион": [53, 84, 58, 68, 92, 72, 54, 38, 96, 54, 52, 87],
        "стрелец": [61, 49, 71, 61, 93, 53, 85, 95, 91, 66, 89, 88],
        "козерог": [58, 95, 72, 63, 88, 49, 45, 64, 40, 84, 78, 91],
        "водолей": [72, 56, 78, 61, 78, 38, 89, 50, 75, 67, 76, 71],
        "рыбы": [45, 92, 39, 72, 52, 63, 68, 65, 82, 69, 46, 76]
    }


async def zz(update, context):
    await update.message.reply_text(
        "Напишите знак зодиака женщины:"
    )

    return 1

WM = ""
M = ""


async def first_response(update, context):
    global WM
    WM = update.message.text
    print(WM)
    await update.message.reply_text(
        "Теперь напишите знак мужчины:")
    return 2


async def result(update, context):
    reply_keyboard = [['/start', '/help', "/info"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    M = update.message.text
    print(WM)
    await update.message.reply_text(f"Ваша совместимость: {women[WM][men[M]]}", reply_markup=markup)
    return ConversationHandler.END


async def color(update, context):
    reply_keyboard = [['/start', '/help', "/info"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    week_color = {
        "понедельник": ["желтый", "сильный и богатый"],
        "вторник": ["розовый", "мудрость и  согласие"],
        "четверг": ["оранжевый", "богатство и успех"],
        "пятница": ["голубой", "наставник демонов"],
        "суббота": ["фиолетовый", "безумный везунчик"],
        "среда": ["зеленый", "мудрость и согласие"],
        "воскресенье": ["темный желтый", "творческий и счастливый"]
    }
    await update.message.reply_text(f" {week_color[week[datetime.datetime.today().weekday()]][1]}", reply_markup=markup)
    return ConversationHandler.END


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('zz', zz)],

        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, first_response)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, result)]
        },

        fallbacks=[CommandHandler('result', result)]
    )
    application.add_handler(conv_handler)

    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, start)
    application.add_handler(text_handler)
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("day", day))
    application.add_handler(CommandHandler("love", love))
    application.add_handler(CommandHandler("where_love", where_love))
    application.add_handler(CommandHandler("future", future))
    application.add_handler(CommandHandler("money", money))
    application.add_handler(CommandHandler("zz", zz))
    application.add_handler(CommandHandler("color", color))
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
