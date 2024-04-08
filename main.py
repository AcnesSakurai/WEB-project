import logging
import datetime
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram import ReplyKeyboardMarkup


BOT_TOKEN = "6316601466:AAGR0OJks7WwNgvbr6gj2uJzHBU47SH0JK0"
reply_keyboard = [['/start', '/help', "/info"]]

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
        caption="Приветствую в нашем уютном боте! Тут вы узнаете будущее и немножко больше) выберите какой расклад вам нужен:"
    )


async def help(update, context):
    await update.message.reply_text(
        "Привет! Я готова тебе помочь с любым возникшим вопросом. Вот что я умею:"
        "1. /start - запускает бота-таролога,"
        "2. /help - выводит список доступных команд,"
        "3. /info - выводит дополнительную информацию о боте-тарологе и дополнительную информацию о гаданиях и значениях карт.")


async def info(update, context):
    await update.message.reply_text(
        "Наш бот не идиален, если Вас заинтересовало гадание, то можете узнать подробнее перейдя по ссылке https://gadalkindom.ru/gadanie/taro/znachenie-kart-taro ")


async def info(update, context):
    await update.message.reply_text(
        "Наш бот не идиален, если Вас заинтересовало гадание, то можете узнать подробнее перейдя по ссылке https://astrohelper.ru/gadaniya/taro/znachenie/ ")


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, start)
    application.add_handler(text_handler)
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("info", info))
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()