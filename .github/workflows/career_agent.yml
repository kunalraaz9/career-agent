import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

jobs = [
    {
        "title": "BEL Recruitment",
        "score": "10/10",
        "link": "https://bel-india.in/"
    },
    {
        "title": "ECIL Careers",
        "score": "10/10",
        "link": "https://www.ecil.co.in/jobs.html"
    },
    {
        "title": "ISRO Careers",
        "score": "10/10",
        "link": "https://www.isro.gov.in/Careers.html"
    },
    {
        "title": "DRDO Careers",
        "score": "10/10",
        "link": "https://www.drdo.gov.in/careers"
    }
]

message = "🚀 Career Agent Daily Report\n\n"

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

print("Report sent")
