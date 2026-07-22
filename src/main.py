import os
from threading import Thread
from flask import Flask
import telebot

# 1. إعداد توكن البوت الخاص بك
TOKEN = "8658764867:AAH9sHro63fGdyNBKGs8b4Ra2qJscnPmYQ"
bot = telebot.TeleBot(TOKEN)


# 2. إنشاء خادم ويب وهمي (لكي يرضى موقع Render ولا يغلق البوت)
app = Flask("")


@app.route("/")
def home():
  return "I am alive and the bot is running!"


def run():
  app.run(host="0.0.0.0", port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()


# 3. أوامر بوت التليجرام
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
  bot.reply_to(message, "أهلاً بك! بوت التليجرام يعمل الآن بنجاح 🚀")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, f"أرسلت لي: {message.text}")


# 4. تشغيل خادم الويب والبوت معاً
if __name__ == "__main__":
  keep_alive()
  bot.infinity_polling()
