import pytest
import requests
import json
import time
from Util.resources import *

"""
Testing response body by requesting GET 10 times.
1. When response status_code is 429, it is due to "Too Many Requests".
2. When response status_code is 200, request is successful.
   2.1. If response returns empty data, then fail the test.
   2.2. Make sure in response body, the type of "name" and "recordLabel" keys is str, type of "bands" key is list. Otherwise fail the test.
"""

def test_body():
#response = requests.get('https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals', headers = {'Content-Type': 'application/json'})
    for i in range(10):
        time.sleep(5)
        print("GET request: " + str(i + 1))
        response = requests.get(resources.endpoint, headers = resources.headers)
        if response.status_code == 429:
            print(response.text)
            continue
        elif response.status_code == 200:
            if len(response.json()) == 0:
                assert False, "No data got!"
            else:
                print(response.json())
                for j in range(len(response.json())):
                    for key in response.json()[j]:
                        if key == 'name' or key == 'recordLabel':
                            assert type(response.json()[j][key]) is str, "Type of {} should be str!".format(key)
                        elif key == 'bands':
                            assert type(response.json()[j][key]) is list, "Type of {} should be list!".format(key)

