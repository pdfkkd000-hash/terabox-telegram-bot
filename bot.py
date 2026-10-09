import os
import re
import logging
from telegram import Update
from telegram.ext import (
Application,
CommandHandler,
MessageHandler,
ContextTypes,
filters,
)

logging.basicConfig(
format="%(asctime)s - %(levelname)s - %(message)s",
level=logging.INFO,
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

URL_PATTERN = re.compile(r"https?://\S+", re.IGNORECASE)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"Welcome to TeraBox Helper! 🎬\n\n"
"Send a TeraBox link to check it.\n"
"Note: This starter bot does not download videos yet."
)

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
text = update.message.text or ""
match = URL_PATTERN.search(text)

if not match:
    await update.message.reply_text("Please send a valid URL.")
    return

url = match.group(0).rstrip(".,)")
if "terabox.com" not in url.lower() and "1024tera.com" not in url.lower():
    await update.message.reply_text(
        "Please send a link from a supported TeraBox domain."
    )
    return

await update.message.reply_text(
    "TeraBox link received ✅\n\n"
    "This starter version can recognize links, but it does not "
    "extract or download video files yet."
)

def main():
if not TOKEN:
raise RuntimeError("TELEGRAM_BOT_TOKEN environment variable is missing.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
app.run_polling()

if name == "main":
main()
