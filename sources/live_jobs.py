import requests
from sources.storage import load_seen_jobs, save_seen_job

def get_live_test():
 seen = load_seen_jobs()

```
job_name = "ECIL Website Reachable"

if job_name not in seen:
    save_seen_job(job_name)

    return [
        (
            "🆕 NEW ENTRY DETECTED",
            "https://www.ecil.co.in/jobs.html",
            "10/10"
        )
    ]

return [
    (
        "No New Entries",
        "",
        "0/10"
    )
]
```
