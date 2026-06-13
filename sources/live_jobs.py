import requests
from bs4 import BeautifulSoup

def get_live_test():
try:
response = requests.get(
"https://www.ecil.co.in/jobs.html",
timeout=15
)

```
    return [
        (
            "ECIL Website Reachable",
            "https://www.ecil.co.in/jobs.html",
            "10/10"
        )
    ]

except Exception as e:
    return [
        (
            f"ERROR: {e}",
            "",
            "0/10"
        )
    ]
```
