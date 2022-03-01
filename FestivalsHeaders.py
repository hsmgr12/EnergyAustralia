import requests
import json
import time
from Util.resources import *

"""
Testing response headers by looping 3 kinds of header 'Content-Type'.
1. When response status_code is 429, it is due to "Too Many Requests".
2. When response status_code is 200, request is successful.
   2.1. Make sure in response headers, the 'connection' is 'keep-alive'. Otherwise fail the test.
   2.2. Make sure in response headers, the 'Content-Type' is as requsted. Otherwise fail the test.
"""
hs = [{'Content-Type': 'application/json'}, {'Content-Type': 'text/plain'}, {'Content-Type': 'text/json'}]
for h in hs:
    time.sleep(5)
    print("testing header Content-Type: " + h['Content-Type'])
    response = requests.get(resources.endpoint, headers = h)
    if response.status_code == 429:
        print(str(response.status_code) + ": " + response.text)
        continue
    elif response.status_code == 200:
        assert response.headers['connection'] == "keep-alive", "Response header connection should be keep-alive!"
        assert h['Content-Type'] in response.headers['Content-Type'], "Response header Content-Type {} should be {}!".format(response.headers['Content-Type'], h['Content-Type'])