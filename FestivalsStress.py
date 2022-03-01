import requests
import json
import time
from Util.resources import *

"""
Stress testing by requesting GET 1000 times, make sure the connection is still 'keep-alive'.
"""
for i in range(1000):
    print("GET request: " + str(i + 1))
    response = requests.get(resources.endpoint, headers = resources.headers)
    assert response.headers['connection'] == "keep-alive", "Response header connection should be keep-alive!"