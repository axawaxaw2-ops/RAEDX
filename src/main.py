import os
from threading import Thread
from flask import Flask
import telebot

TOKEN = "8658764867:AAElz0WXlaKML9IwgLmesv1_0Sgsn5UH7E"
bot = telebot.TeleBot(TOKEN)

# مسح أي ويب هوك قديم عالق لدى تليجرام فوراً
try:
    bot.remove_webhook()
except Exception as e:
    print(e)

# سيرفر ويب وهمي لكي يرضى موقع Render
app = Flask("app")

@app.route("/")
def home():
    return "I am alive and the bot is running!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# دالة تشغيل البوت
def run_bot():
    print("Bot started polling...")
    bot.infinity_polling(none_stop=True)

if __name__ == "__main__":
    keep_alive()
    run_bot()
