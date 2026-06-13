import os
import requests
from sources.psu import get_psu_jobs
from sources.govt import get_govt_jobs
from sources.remote import get_remote_jobs
from sources.core import get_core_jobs
from sources.bel import get_bel_jobs
from sources.ecil import get_ecil_jobs
from sources.ntpc import get_ntpc_jobs
from sources.powergrid import get_powergrid_jobs

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

message = "DAILY CAREER REPORT\n\n"

message += "PSU JOBS\n"
for name, link, score in get_psu_jobs():
    message += "\n" + name + "\nScore: " + str(score) + "\n" + link + "\n"

message += "\nLIVE BEL JOBS\n"
for name, link, score in get_bel_jobs():
    message += "\n" + name + "\nScore: " + str(score) + "\n" + link + "\n"

message += "\nLIVE ECIL JOBS\n"
for name, link, score in get_ecil_jobs():
    message += "\n" + name + "\nScore: " + str(score) + "\n" + link + "\n"

message += "\nLIVE NTPC JOBS\n"
for name, link, score in get_ntpc_jobs():
    message += "\n" + name + "\nScore: " + str(score) + "\n" + link + "\n"

message += "\nLIVE POWERGRID JOBS\n"
for name, link, score in get_powergrid_jobs():
    message += "\n" + name + "\nScore: " + str(score) + "\n" + link + "\n"

message += "\nCORE ELECTRICAL & ELECTRONICS JOBS\n"
for name, link, score in get_core_jobs():
    message += "\n" + name + "\nScore: " + str(score) + "\n" + link + "\n"

message += "\nGOVERNMENT EXAMS\n"
for name, link, score in get_govt_jobs():
    message += "\n" + name + "\nScore: " + str(score) + "\n" + link + "\n"

message += "\nREMOTE JOBS\n"
for name, link, score in get_remote_jobs():
    message += "\n" + name + "\nScore: " + str(score) + "\n" + link + "\n"

url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print(response.text)
