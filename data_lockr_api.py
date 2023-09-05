"""
API Version: v1
Author: Ritika Arora
script to test dataLockr APIs using Python3 requests.
"""

import json
import requests

BASE_URL = "http://127.0.0.1:8000"


def get_token(params):
    """function to get user token"""
    get_jwt_token = requests.post(
        f'{BASE_URL}/api/token/',  params)

    result = json.loads(get_jwt_token.text)
    print(result['access'])

user_details={
    'username': 'ritika.1',
    'password': 'Confirm@121' 
        }
get_token(user_details)
