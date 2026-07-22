import os
from threading import Thread
from flask import Flask
import telebot

# إعداد توكن البوت الخاص بك
TOKEN = "8658764867:AAH9sHro63fGdyNBKGs8b4Ra2qJscnPmtYQ"
bot = telebot.TeleBot(TOKEN)

# إنشاء خادم ويب وهمي لكي يرضى موقع Render
app = Flask("app")

@app.route("/")
def home():
    return "I am alive and the bot is running!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# دالة لتشغيل البوت في الخلفية بشكل صحيح
def run_bot():
    bot.infinity_polling(none_stop=True)

if __name__ == "__main__":
    keep_alive()
    run_bot()

