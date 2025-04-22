

---

# 🤖 Telegram FaceSwap Bot

A powerful and easy-to-use **FaceSwap Bot** built with Python and the **FaceSwap API**, with **imgbb** for image hosting and deployed on **Railway**.

> ⚡ Built by [@AnshApi](https://t.me/AnshApi)

---

## 📸 How It Works

1. User sends **two images** to the bot:
   - First image = **Source face**
   - Second image = **Target image** (face will be swapped into this)
2. The bot uploads both images to imgbb.
3. It sends the URLs to the **FaceSwap API**.
4. The API returns the **swapped result**, which is sent back to the user.

---

## 🚀 Features

- Instant image face swapping
- Hosted on Railway
- User-friendly Telegram interface
- Uses **imgbb** for image uploads
- Built using `python-telegram-bot` (async)

---

## 🌐 API Services Used

- 🔁 [FaceSwap API](https://faceswap.ytansh038.workers.dev/)
- ☁️ [imgbb Image Hosting](https://api.imgbb.com/)

---

## 🧰 Requirements

- Python 3.10+
- Telegram Bot Token
- imgbb API Key
- Railway account for deployment

---

## 🔧 Setup Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/telegram-faceswap-bot.git
   cd telegram-faceswap-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create `.env` file**
   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   IMGBB_API_KEY=your_imgbb_api_key
   ```

4. **Run the bot**
   ```bash
   python bot.py
   ```

---

## 🚀 Deploy on Railway

> Railway is a PaaS that makes deploying apps super simple.

1. Go to [Railway.app](https://railway.app/)
2. Click **"New Project" → "Deploy from GitHub Repo"**
3. Select your repository
4. **Set Environment Variables** in Railway:
   - `TELEGRAM_BOT_TOKEN` = *your Telegram bot token*
   - `IMGBB_API_KEY` = *your imgbb key*
5. Deploy 🚀

---

## 🧠 Bot Commands

- `/start` → Start the bot, view welcome message & buttons
- **Send 2 photos** → 1st is source, 2nd is target → get swapped face!

---

## 📂 File Structure

```bash
telegram-faceswap-bot/
├── bot.py                # Main bot logic
├── requirements.txt      # Dependencies
└── README.md             # You’re here!
```

---

## 📦 requirements.txt

```txt
python-telegram-bot==20.7
requests
```

---

## 🙋 Support

For help or questions, message [@AnshApi](https://t.me/AnshApi)

---

## 📄 License

MIT License – do anything, just credit the original author.

---

Let me know if you want this in ZIP format or want to include a `.env.example` template as well!
