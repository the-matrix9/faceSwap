## 🔁 Telegram FaceSwap Bot using FaceSwap API + imgbb for image hosting

import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🔐 Your bot token and imgbb key
TELEGRAM_BOT_TOKEN = "APNA BOT TON DALO NA MERI JAAN "
IMGBB_API_KEY = "Apna API DALO YRR  "

# 🧠 Store users' source/target image URLs
user_sessions = {}

## ⬆ Upload image to imgbb and return image URL
def upload_to_imgbb(file_bytes):
    url = "https://api.imgbb.com/1/upload"
    payload = {"key": IMGBB_API_KEY}
    files = {"image": file_bytes}
    response = requests.post(url, data=payload, files=files)
    try:
        data = response.json()
        if data["success"]:
            return data["data"]["url"]
    except:
        return None

## 🔘 /start command with welcome image and buttons
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("👤 Owner", url="https://t.me/AnshApi"),
         InlineKeyboardButton("💬 Support", url="https://t.me/AnshApi")],
        [InlineKeyboardButton("🔄 Join Channel", url="https://t.me/AnshApi")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    caption = (
        "👋 Welcome to **FaceSwap Bot**!\n\n"
        "📸 Send me 2 images:\n"
        "1. Source face (first)\n"
        "2. Target image (where to swap the face)\n\n"
        "⚡ I'll send you a face swapped result instantly!\n"
        "_Built with ❤️ by @AnshApi_"
    )

    await update.message.reply_photo(
        photo="https://envs.sh/KMm.jpg",  # You can replace this with any hosted image
        caption=caption,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

## 📸 Handle all photo messages (source and target detection)
async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)
    file_bytes = await file.download_as_bytearray()

    image_url = upload_to_imgbb(file_bytes)
    if not image_url:
        await update.message.reply_text("❌ Failed to upload image. Try again.")
        return

    # First image = source
    if user_id not in user_sessions:
        user_sessions[user_id] = {"source": image_url}
        await update.message.reply_text("Now send the **target image**.")
    else:
        user_sessions[user_id]["target"] = image_url
        processing_msg = await update.message.reply_text("⚙️ Swapping faces, please wait...")

        source = user_sessions[user_id]["source"]
        target = user_sessions[user_id]["target"]
        api_url = f"https://faceswap.ytansh038.workers.dev/?imageurl={source}&targetimg={target}"

        try:
            response = requests.get(api_url)
            data = response.json()
            if data["status"]:
                result_url = data["result"]
                await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=processing_msg.message_id)
                await update.message.reply_photo(photo=result_url, caption="✅ Face swapped successfully!\n_By @AnshAp")
            else:
                await update.message.reply_text("❌ FaceSwap failed. Try again.")
        except Exception as e:
            await update.message.reply_text(f"⚠️ Error: {e}")

        user_sessions.pop(user_id)

## 🚀 Bot start
if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))

    print("🤖 FaceSwap Bot by @AnshApi is running...")
    app.run_polling()
