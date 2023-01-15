import os
import telegram
from constants import API_KEY

def telegram_bot(request):
    bot = telegram.bot(API_KEY)
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        bot.sendMessage(chat_id=chat_id, text=update.message.text)
    return "test"