import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

message = """
🚀 Career Agent Started

Version 1 Active

Sections:
✅ Core Engineering Jobs
✅ PSU Jobs
✅ Government Exams
✅ Remote Jobs

More sources coming soon.
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print("Message sent successfully")
