from telegram import Update
from telegram.ext import Updater,CallbackContext, CommandHandler



def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

updater = Updater('5705249953:AAGV_LOWqev5-Q2m2EIkqHyckMxHTvCYuvM')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()