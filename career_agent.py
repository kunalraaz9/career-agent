import os
import requests
from sources.psu import get_psu_jobs

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

jobs = get_psu_jobs()

message = "🚀 DAILY CAREER REPORT\n\n"
message += "🏛 PSU / GOVERNMENT JOBS\n\n"

for job in jobs:
    message += (
        f"🔥 {job['title']}\n"
        f"Match Score: {job['score']}\n"
        f"Apply: {job['link']}\n\n"
    )

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print("Report Sent")
