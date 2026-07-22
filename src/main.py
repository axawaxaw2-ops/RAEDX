from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🦅 أهلاً بك في RAED X\n\nالبوت يعمل بنجاح ✅"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("RAED X Bot Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
