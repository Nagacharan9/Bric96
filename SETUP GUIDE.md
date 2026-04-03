# 🚀 SETUP GUIDE — Trade Signal App
### (Read this fully before starting — super easy!)

---

## 📦 FILES YOU HAVE
- `server.py` → your cloud brain
- `requirements.txt` → libraries for server
- `Procfile` → tells Render how to run
- `index.html` → your BUY/SELL screen
- `SETUP GUIDE.md` → this file

---

## 🟢 STAGE 1 — Create Free Accounts (10 mins)

### 1. GitHub (free)
- Go to https://github.com
- Click "Sign up"
- Use any email + password
- Verify email ✅

### 2. Render (free)
- Go to https://render.com
- Click "Get Started for Free"
- Sign up WITH your GitHub account (easier!)
- ✅ Done

---

## 🟢 STAGE 2 — Upload Code to GitHub (5 mins)

1. Login to GitHub
2. Click the **"+"** icon (top right) → **"New repository"**
3. Name it: `trade-signal-app`
4. Keep it **Public**
5. Click **"Create repository"**
6. Click **"uploading an existing file"** link
7. Drag and drop these 3 files:
   - `server.py`
   - `requirements.txt`
   - `Procfile`
8. Click **"Commit changes"**
9. ✅ Code is now on GitHub!

---

## 🟢 STAGE 3 — Deploy on Render (5 mins)

1. Go to https://render.com → Login
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub → Select `trade-signal-app`
4. Fill in settings:
   - **Name**: trade-signal-app
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python server.py`
   - **Plan**: Free ✅
5. Click **"Create Web Service"**
6. Wait 2-3 minutes for deploy
7. You get a URL like: `https://trade-signal-app.onrender.com`
8. **COPY THIS URL** — you need it!

---

## 🟢 STAGE 4 — Keep Server Awake FREE (3 mins)

(So Render never sleeps and you miss no signals!)

1. Go to https://uptimerobot.com
2. Sign up free
3. Click **"Add New Monitor"**
4. Monitor Type: **HTTP(s)**
5. URL: `https://your-app.onrender.com/ping`
6. Interval: **5 minutes**
7. Click Save ✅

---

## 🟢 STAGE 5 — Open Your Signal Screen (1 min)

1. Open `index.html` in your browser
   (just double-click the file)
2. Paste your Render URL in the box at bottom
3. Click **Connect**
4. Status shows **"Live — Connected"** ✅
5. Put this on RIGHT HALF of screen
6. Put TradingView on LEFT HALF

---

## 🟢 STAGE 6 — TradingView Alert Setup (5 mins)

### What to paste in TradingView Webhook URL:
```
https://your-app.onrender.com/webhook
```

### What message to send (Alert Message box):
**For BUY signal:**
```json
{"signal": "BUY", "pair": "EURUSD"}
```

**For SELL signal:**
```json
{"signal": "SELL", "pair": "EURUSD"}
```

### How to set alert:
1. Open your chart on TradingView
2. Right-click on your indicator → **"Add Alert"**
3. Set condition to when arrow appears
4. Scroll down to **"Webhook URL"**
5. Paste: `https://your-app.onrender.com/webhook`
6. In **"Message"** box paste the JSON above
7. Click **"Create"** ✅

---

## ✅ YOU'RE DONE!

```
TradingView arrow fires
       ↓ (under 1 second)
Your right screen flashes
BUY 🟢  or  SELL 🔴
       ↓
You place trade on Exnova
```

---

## ❓ Stuck Anywhere?
Just come back to Claude and say which stage you're stuck on!
I'll help you step by step 💪
