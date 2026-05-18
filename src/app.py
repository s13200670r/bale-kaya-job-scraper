from bale_bot import send_to_bot
from datetime import datetime
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read SKILL_IDS=95,1075,3113,2918
raw_ids = os.getenv("SKILL_IDS", "")
skill_ids = [int(x.strip()) for x in raw_ids.split(",") if x.strip()]


while True:
    count = 0

    for skill_id in skill_ids:
        count += send_to_bot(skill_id)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] check completed — {count} project(s) sent")

    if count > 0:
        os.system("paplay /usr/share/sounds/freedesktop/stereo/complete.oga")
        os.system('notify-send "New Project" "A new project found! Horaaaaaaaaaaaaaaaaaaa!"')

    time.sleep(180)

