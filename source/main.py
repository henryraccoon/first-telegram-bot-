import os
import telebot 
from telebot import types

def telegram_bot():
    
    bot = telebot.TeleBot(token=os.environ["TELEGRAM_TOKEN"], parse_mode=None)



    @bot.message_handler(commands=["start"])
    def send_welcome_message(msg):
        bot.reply_to(msg, "... you woke me up. what?")
        print(msg)

    @bot.message_handler(commands=["help"])
    def send_help_message(msg):
        bot.reply_to(msg, "if you need help go ask google. I'm a cat!")
        print(msg)

    @bot.message_handler(commands=["hello"])
    def send_help_message(msg):
        bot.reply_to(msg, "meow-meow")
        print(msg)



    @bot.message_handler(content_types=["photo", "sticker", "audio", "video", "document"])
    def send_content_message(msg):
        bot.reply_to(msg, "wow. can you just go back to text? i dunno what to say...")    

    @bot.message_handler(commands = ["get info", "info"])
    def get_bot_info(msg):
        markup_inline = types.InlineKeyboardMarkup()
        item_yes = types.InlineKeyboardButton(text = "YEAH", callback_data = "yes")
        item_no = types.InlineKeyboardButton(text = "NAH", callback_data = "no")

        markup_inline.add(item_yes, item_no)
        bot.send_message(msg.chat.id, "I'm grumpy... do you want to make me happy?", reply_markup = markup_inline)


    @bot.callback_query_handler(func = lambda call: True)
    def answer(call):
        if call.data == "yes":
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item_feed = types.InlineKeyboardButton("FEED 🍗")
            item_pet = types.InlineKeyboardButton("PET 🫳")
            item_play = types.InlineKeyboardButton("PLAY 🎾")

            markup_reply.add(item_feed, item_pet, item_play)
            bot.send_message(call.message.chat.id, "okay choose something...", reply_markup = markup_reply)
        elif call.data == "no":
            pass


    @bot.message_handler(content_types = ["text"])
    def get_text(msg):
        if msg.text.lower() in ("hello", "hi", "sup", "hey", "yo", "good morning", "whatsup", "привіт", "привет", "你好"):
            bot.send_message(msg.chat.id, "meow, hi")
        elif msg.text.lower() in ("sonia", "sonichka", "sonika", "soso", "baby girl", "sonini", "cutie", "babygirl"):
            bot.send_message(msg.chat.id, "that's my name, yes. what do you want? do you have food for me? no?")
        elif msg.text.lower() in ("who are you?", "who are you", "what are you?", "what are you", "tell about yourself", "tell me about yourself"):
            bot.send_message(msg.chat.id, "I'm Sonia. Thre prettiest cat in the world. Also with the best personality. Born in China, but actually half ukrainian half bruneian.")
        elif msg.text.lower() in ("what do you like?", "what do you like", "what do you like to do?", "what do you like to do", "what do you do?", "what do you do"):
            bot.send_message(msg.chat.id, "I like to eat, sleep, and play. Sometimes hunt 🦎🪳🐞🐀, talk to birds and allow those humans pet me and give me massage or comb my perfect fur.")
        elif msg.text.lower() in ("what do you love?", "what do you love", "who do you love?", "who do you love,", "do you love anyone?", "do you love anyone", "do you love mommy?", "do you love mummy?"):
            bot.send_message(msg.chat.id, "i love noone!!!")
            bot.send_message(msg.chat.id, "okay. i love mummy.")
            
        elif msg.text.lower() in ("do you love daddy?", "do you love daddy"):
            bot.send_message(msg.chat.id, "i don't remember my daddy. and i never liked him anyway. only his chicken.")    
        elif msg.text.lower() in ("how are you?", "how are you", "how are you doing?", "how're you doing?", "how're you doing", "how are you doing"):
            bot.send_message(msg.chat.id, "use command /info")
        elif msg.text.lower() in ("bye", "bye bye", "good bye", "see you", "see ya", "have a good day"):
            bot.send_message(msg.chat.id, "yeah, whatever")
        elif msg.text.lower() in ("i love you", "i love you!", "i love u", "i love you!!!"):
            bot.send_message(msg.chat.id, "everyone loves me. I'm perfect")
        elif msg.text.lower() in ("bitch", "bitch!", "little bitch", "little bitch!", "you're a bitch!", "you're a bitch", "you are a bitch"):
            bot.send_message(msg.chat.id, "what did you say?? do you wanna fight?? *bit leg*")

        elif msg.text == ("FEED 🍗"):
            bot.send_message(msg.chat.id, "I only accept chicken cooked by my dad, or treats from my mum. otherwise, no, thank you.")
        elif msg.text == ("PET 🫳"):
            bot.send_message(msg.chat.id, "wrong! *ran away*")
        elif msg.text == ("PLAY 🎾"):
            bot.send_message(msg.chat.id, "I'm READY! lets play fetch! yes! no, im not a dog. just throw that piece of trash now!!")
        else:
            bot.send_message(msg.chat.id, "meow")

    bot.polling()
telegram_bot()