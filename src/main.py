import os
from flask import Flask, request
import telebot

TOKEN = "8658764867:AAHfWGPjjmvPqGazA894ujhtG3uVipl11I8"
bot = telebot.TeleBot(TOKEN)

app = Flask("app")

# مسار استقبال الرسائل من تليجرام (Webhook)
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def home():
    return "Bot is running via Webhook!"

if __name__ == "__main__":
    # ربط البوت برابط موقعك على Render تلقائياً
    bot.remove_webhook()
    bot.set_webhook(url=f"https://raedx.onrender.com/{TOKEN}")
    
    # تشغيل سيرفر الويب
    app.run(host="0.0.0.0", port=8080)
