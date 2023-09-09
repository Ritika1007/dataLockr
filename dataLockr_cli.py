"""
API Version: v1
Author: Ritika Arora
CLI for handling CRUD via dataLockr APIs using Python3 requests.
"""

import json
import getpass
from termcolor import cprint
import requests


BASE_URL = "http://127.0.0.1:8000"

def get_header(token):
    """"
    function to return header as dict for python requests 
    """
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    return headers


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

#folder operations
def get_folders_list(token):
    """get lits of folders created by user"""
    end_point = '/v1/api/subfolders/'

    result = requests.get(
        f'{BASE_URL}{end_point}', headers=get_header(token)
    )
    cprint(json.dumps(json.loads(result.text), indent=4, sort_keys=True), 'green')

def create_folder(token,payload):
    """create folder"""
    end_point = '/v1/api/subfolders/'

    result = requests.post(
        f'{BASE_URL}{end_point}', headers=get_header(token), data=payload
    )
    cprint(json.dumps(json.loads(result.text), indent=4, sort_keys=True), 'green')
    
    
def delete_folder(token,id):
    """function to delete folder"""
    end_point = f'/v1/api/subfolders/{id}'

    result = requests.delete(
        f'{BASE_URL}{end_point}', headers=get_header(token)
    )
    cprint(result, 'green')
    
#file operations    
def get_files_in_folders(token,folder_id):
    """get lits of files in a folder created by user"""
    end_point = f'/v1/api/subfolders/{folder_id}/files'

    result = requests.get(
        f'{BASE_URL}{end_point}', headers=get_header(token)
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


# folder = input('Enter Subfolder ID: ')
# get_files_in_folders(access_token,folder)


payload = json.dumps({
  "name": "requestsTest"
})

# create_folder(access_token,payload)
cprint("Note: all files under this will be deleted.", 'red')
folder_to_delete = input('Enter Subfolder ID: ')
delete_folder(access_token, folder_to_delete)