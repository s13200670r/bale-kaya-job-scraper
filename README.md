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
```

# 🚀 Getting Started

## 1. Prerequisites

Make sure you have Python 3.x installed. You also need to create a bot on Bale via BotFather to get your token.

## 2. Installation

Clone the repository and install the dependencies:

```
bash
pip install -r requirements.txt
```

## 3. Configuration

Copy the example environment file and fill in your details:

```
bash
cp .env.example .env
```

Edit `.env` and add your credentials:

```
env
BALE_TOKEN=your_bot_token_here
CHAT_ID=your_personal_chat_id
SKILL_IDS=95,1075,3113,2918
```

## 4. Running the Bot

To start the monitoring process, run:

```
bash
python src/app.py
```

## 📝 Configuration Details

- **SKILL_IDS**: Comma-separated IDs of the skills you want to track.
- **sent_projects.json**: This file is automatically created in the `data/` folder to keep track of project history.

## ⚠️ Requirements

- `python-dotenv`
- `requests`
- *(Optional)* `paplay` and `libnotify-bin` for Linux sound/desktop alerts.

## 📜 License

This project is open-source and available under the MIT License.
