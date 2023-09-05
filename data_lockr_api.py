"""
API Version: v1
Author: Ritika Arora
script to test dataLockr APIs using Python3 requests.
"""

import json
import getpass
from termcolor import cprint
import requests


BASE_URL = "http://127.0.0.1:8000"


def get_token(params):
    """function to get user jwt token"""
    get_jwt_token = requests.post(
        f'{BASE_URL}/api/token/',  params)

    result = json.loads(get_jwt_token.text)
    try:
        return result['access']
    except KeyError:
        cprint('\nInvaid User!','red')


#Get User Creds
username = input('Enter Username: ')
password = getpass.getpass(prompt='Enter Passowrd: ')

user_details={
    'username': username,
    'password': password 
        }
get_token(user_details)
