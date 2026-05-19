# Bale Kaya Bot 🚀

An automated Python tool to monitor **Kaya** projects and receive instant notifications via **Bale Messenger**. This bot checks for new projects based on specific Skill IDs and ensures you never miss an opportunity.

## 🛠 Features
- **Real-time Monitoring:** Checks for new projects every few minutes.
- **Bale Integration:** Sends project details directly to your Bale chat.
- **Smart Filtering:** Uses `sent_projects.json` to prevent duplicate notifications.
- **Environment Configurable:** Easily manage tokens and IDs using a `.env` file.
- **Desktop Alerts:** Supports system sounds and notifications (Linux/Ubuntu).

## 📂 Project Structure
```text
BALE KAYA BOT/
├── data/
│   └── sent_projects.json    # Database of already notified projects
├── src/
│   ├── app.py                # Main entry point (the loop)
│   ├── bale_bot.py           # Logic for sending messages to Bale
│   └── kaya_scraper.py       # Scraper logic to fetch projects from Kaya
├── .env                      # Local secret configurations (Ignored by Git)
├── .env.example              # Template for environment variables
├── .gitignore                # Files to be excluded from Git
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── kaya.json                 # Kaya skill ids list
