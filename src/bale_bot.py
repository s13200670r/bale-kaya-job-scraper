import requests
from kaya_scraper import kaya_scraper
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BALE_TOKEN = os.getenv("BALE_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

BASE_URL = f"https://tapi.bale.ai/bot{BALE_TOKEN}"

def send_to_bot(skill_id):
    projects = kaya_scraper(skill_id)

    for text in projects:
        requests.post(
            f"{BASE_URL}/sendMessage",
            json={
                "chat_id": CHAT_ID,
                "text": text
            }
        )

    return len(projects)
