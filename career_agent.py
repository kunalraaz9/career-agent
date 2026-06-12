import os
import requests

from sources.psu import get_psu_jobs
from sources.govt import get_govt_jobs
from sources.remote import get_remote_jobs
from sources.core import get_core_jobs
from sources.bel import get_bel_jobs

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

message = "🚀 DAILY CAREER REPORT\n\n"

message += "🏛 PSU JOBS\n"
for name, link, score in get_psu_jobs():
    message += f"\n{name}\nScore: {score}\n{link}\n"

message += "🔥 LIVE BEL JOBS\n"

for name, link, score in get_bel_jobs():
    message += f"\n{name}\nScore: {score}\n{link}\n"
message += "\n⚡ CORE ELECTRICAL JOBS\n"

for name, link, score in get_core_jobs():
    message += f"\n{name}\nScore: {score}\n{link}\n"

message += "\n\n📢 GOVERNMENT EXAMS\n"
for name, link, score in get_govt_jobs():
    message += f"\n{name}\nScore: {score}\n{link}\n"

message += "\n\n🌍 REMOTE JOBS\n"
for name, link, score in get_remote_jobs():
    message += f"\n{name}\nScore: {score}\n{link}\n"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print(response.text)
