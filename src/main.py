import telebot

TOKEN = "8658764867:AAHfWGPjjmvPqGazA894ujhtG3uVipl11I8"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! البوت يعمل بنجاح تام 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"لقد أرسلت: {message.text}")

print("Bot is running...")
bot.infinity_polling()
