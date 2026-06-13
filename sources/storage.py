def load_seen_jobs():
try:
with open("data/seen_jobs.txt", "r") as f:
return set(f.read().splitlines())
except:
return set()

def save_seen_job(job):
with open("data/seen_jobs.txt", "a") as f:
f.write(job + "\n")
