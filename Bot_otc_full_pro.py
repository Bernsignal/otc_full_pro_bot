import telebot
import time
import random
import threading

TOKEN = "METE_TOKEN_OU_ISIT"

bot = telebot.TeleBot(TOKEN)

chat_id_global = None

@bot.message_handler(commands=['start'])
def start(message):
    global chat_id_global
    chat_id_global = message.chat.id
    bot.send_message(chat_id_global, "🤖 Bot la aktif! Signal ap kòmanse...")

def send_signal():
    global chat_id_global
    while True:
        if chat_id_global is not None:
            signal = random.choice(["📈 BUY", "📉 SELL"])
            bot.send_message(chat_id_global, f"🚀 SIGNAL: {signal}")
        time.sleep(60)

threading.Thread(target=send_signal).start()

bot.polling()
