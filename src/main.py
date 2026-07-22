import os
from threading import Thread
from flask import Flask
import telebot

TOKEN = "8658764867:AAHfWGPjjmvPqGazA894ujhtG3uVipl11I8"
bot = telebot.TeleBot(TOKEN)

# سيرفر ويب وهمي لكي يرضى موقع Render ويظل البوت شغّالاً
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
