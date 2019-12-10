import logging

import numberOCR
import ocr

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import Bot

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Sand a captcha image to get text response')


def getTextFromImage(update, context):
    if not update.message.caption:
        context.bot.sendMessage(chat_id=update.message.chat_id, text="Please choose 1 or 2")
        return
    print("Downloading image...")
    fileID = update.message.photo[-1].file_id
    newFile = context.bot.getFile(fileID)
    path = "./temp/"
    fileName = "image.jpg"
    newFile.download(path + fileName)
    print("Downloaded succesfully")
    caption = update.message.caption
    output = ""
    if caption == "1":
        output = numberOCR.detectNumber(path+fileName)
    if caption == "2":
        output = ocr.detectText(path+fileName)
    print(output)
    context.bot.sendMessage(chat_id=update.message.chat_id, text="My answer is: " + output)
    # return captcha(path + fileName, caption)


def echo(update, context):
    context.bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater('TOKEN HERE', use_context=True,
                      base_url="https://telegg.ru/orig/bot")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, getTextFromImage))
    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()
    print("*BOT STARTED*")
    updater.idle()


if __name__ == '__main__':
    main()
