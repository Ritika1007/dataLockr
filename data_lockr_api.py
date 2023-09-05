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
    end_point = '/api/token/'
    get_jwt_token = requests.post(
        f'{BASE_URL}{end_point}',  params)

    result = json.loads(get_jwt_token.text)
    try:
        return result['access']
    except KeyError:
        cprint('\nInvaid User!', 'red')


def get_folders_list(token):
    """get lits of folders created by user"""
    end_point = '/v1/api/subfolders/'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    result = requests.get(
        f'{BASE_URL}{end_point}', headers=headers
    )
    cprint(json.dumps(json.loads(result.text), indent=4, sort_keys=True), 'green')


# Get User Creds
username = input('Enter Username: ')
password = getpass.getpass(prompt='Enter Passowrd: ')

user_details = {
    'username': username,
    'password': password
}
access_token = get_token(user_details)
get_folders_list(access_token)
