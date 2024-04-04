import logging
import datetime
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram import ReplyKeyboardMarkup


BOT_TOKEN = "6316601466:AAGR0OJks7WwNgvbr6gj2uJzHBU47SH0JK0"
reply_keyboard = [['/start', '/date', "/set"],
                  ['/time', '/help', "/unset"]]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TIMER = 5


async def start(update, context):
    img = open('card.png', 'rb')
    await context.bot.send_photo(
        update.message.chat_id,
        img,
        caption="Приветствую в нашем уютном боте! Тут вы узнаете будущее и немножко больше) выберите какой расклад вам нужен:"
    )


async def help(update, context):
    await update.message.reply_text(
        "Я бот справочник.")


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    text_handler = MessageHandler(filters.TEXT, start)
    application.add_handler(text_handler)
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("start", start))
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
