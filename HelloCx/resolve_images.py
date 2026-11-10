
import requests
import re
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urls = [
    "https://ibb.co/CsBRCj7s",
    "https://ibb.co/KxQHsMYk",
    "https://ibb.co/snqcRfd",
    "https://ibb.co/VpQGTDvQ",
    "https://ibb.co/6J7pqmx4",
    "https://ibb.co/LhnmDRbD",
    "https://ibb.co/G4V5fDR7",
    "https://ibb.co/SwZgPJzN",
    "https://ibb.co/jPt0Ht0q",
    "https://ibb.co/zHJPgFdW",
    "https://ibb.co/391RxTj8",
    "https://ibb.co/GQxDkmZC",
    "https://ibb.co/pj7Vd7r2",
    "https://ibb.co/k6zDL1FT",
    "https://ibb.co/NdzfW3Zz",
    "https://ibb.co/M57fFF6V",
    "https://ibb.co/s9nPGFZY",
    "https://ibb.co/4RVgJY1q",
    "https://ibb.co/SwZgPJzN",
    "https://ibb.co/MxLTYjQs",
    "https://ibb.co/ycxtLRSV",
    "https://ibb.co/xtgLG6cN",
    "https://ibb.co/hqMP167",
    "https://ibb.co/nNvvZcR7",
    "https://ibb.co/v6X4GJTR"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

results = {}

for url in urls:
    success = False
    for attempt in range(3):
        try:
            r = requests.get(url, headers=headers, timeout=10, verify=False)
            match = re.search(r'<meta property="og:image" content="([^"]+)"', r.text)
            if match:
                print(f'"{url}": "{match.group(1)}",')
                results[url] = match.group(1)
                success = True
                break
        except Exception as e:
            pass
        time.sleep(1)
    
    if not success:
        print(f'"{url}": "FAILED",')
