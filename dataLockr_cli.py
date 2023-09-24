"""
API Version: v1
Author: Ritika Arora
CLI for handling CRUD via dataLockr APIs using Python3 requests.
"""

import json
import getpass
from termcolor import cprint,colored
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
    """
    function to get user jwt token
    """
    end_point = '/api/token/'
    get_jwt_token = requests.post(
        f'{BASE_URL}{end_point}',  params)

    result = json.loads(get_jwt_token.text)
    try:
        return result['access']
    except KeyError:
        cprint('\nInvaid User!', 'red')
        
####################
#folder operations
####################

def get_folders_list(token):
    """
    get lits of folders created by user
    """
    end_point = '/v1/api/subfolders/'

    result = requests.get(
        f'{BASE_URL}{end_point}', headers=get_header(token)
    )
    # cprint(json.dumps(json.loads(result.text), indent=4, sort_keys=True), 'green')
    list_folders = json.loads(result.text)
    cprint("\nID    Folder\n",'green')
    for data in list_folders:
        cprint(str(data['id'])+'    '+data['name'],'green')

#############################
def create_folder(token,payload):
    """create folder"""
    end_point = '/v1/api/subfolders/'

    result = requests.post(
        f'{BASE_URL}{end_point}', headers=get_header(token), data=payload
    )
    cprint(json.dumps(json.loads(result.text), indent=4, sort_keys=True), 'green')
    # return(json.dumps(json.loads(result.text), indent=4, sort_keys=True))

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
    # return(json.dumps(json.loads(result.text), indent=4, sort_keys=True))
    list_files = json.loads(result.text)
    cprint("\nID    Folder    Content\n",'green')
    for data in list_files:
        cprint(str(data['id'])+'    '+data['name']+'    '+data['content'],'green')

def create_file_in_folder(token,folder_id,payload):
    """create file"""
    end_point = f'/v1/api/subfolders/{folder_id}/files'

    result = requests.post(
        f'{BASE_URL}{end_point}', headers=get_header(token), data=payload
    )
    cprint(json.dumps(json.loads(result.text), indent=4, sort_keys=True), 'green')

def delete_file(token,folder_id,file_id):
    """function to delete file"""
    end_point = f'/v1/api/subfolders/{folder_id}/file/{file_id}'

    result = requests.delete(
        f'{BASE_URL}{end_point}', headers=get_header(token)
    )
    cprint(result, 'green')
    


def user_prompt():
    """
    print user prompts with green color
    """
    return (colored('Enter Your Choice\n\t', 'light_green'))

def get_usercreds():
    """
    Get User Creds for token
    """
    username = input('Enter Username: ')
    password = getpass.getpass(prompt='Enter Passowrd: ')

    user_details = {
        'username': username,
        'password': password
    }
    
    return user_details
    
print()
cprint("#################\n DataLockr CLI\n#################\n","blue")
cprint("What would you like to do?\n","yellow")
cprint("Options\n\t1. CRUD on folders \n\t2. CRUD on files\n","magenta")

choice_param = input(user_prompt()+('(1/2/exit): '))
print()


if choice_param == '1':
    #CRUD on folder
    cprint("-----------------\n CRUD on folders\n-----------------\n","cyan")
    cprint("Options\n\t1. Retrieve list of folders.\n\t2. Create Folder.\n\t3. Delete Folder\n","magenta")
    choice_param = input(user_prompt()+('(1/2/3/exit): '))
    
    if choice_param != "exit":
        user = get_usercreds()
        access_token = get_token(user)
    
        if choice_param == '1': 
            get_folders_list(access_token)
            
        elif choice_param == '2':
            folder_name = input(colored("Enter folder name you want to create: ", 'light_green'))
            payload = json.dumps({
                "name": folder_name
                })
            create_folder(access_token,payload)

        elif choice_param == '3':
            get_folders_list(access_token)
            print()
            folder_id = int(input(colored("Enter folder Id you want to delete: ", 'red')))
            delete_folder(access_token, folder_id)
            
            

            
    else:
        exit(101)
        
elif choice_param == '2':
    #CRUD on files
    cprint("-----------------\n CRUD on Files\n-----------------\n","cyan")
    cprint("Options\n\t1. Retrieve list of files.\n\t2. Create file.\n\t3. Delete file.\n\t4. Update a file.\n","magenta")
    choice_param = input(user_prompt()+('(1/2/3/4/exit): '))
    
    if choice_param != "exit":
        user = get_usercreds()
        access_token = get_token(user)
        
        if choice_param == '1': 
            get_folders_list(access_token)
            folder_id = int(input(colored("\nEnter folder Id : ", 'light_blue')))
            get_files_in_folders(access_token,folder_id)

        elif choice_param == '2':
            get_folders_list(access_token)
            folder_id = int(input(colored("\nEnter folder Id : ", 'light_blue')))
            print()
            file_name = input(colored("Enter file name you want to create: ", 'light_green'))
            file_content = input(colored("Enter file contents: ", 'light_green'))

            payload = json.dumps({
                "name": file_name,
                "content": file_content
                })
            create_file_in_folder(access_token,folder_id,payload)
            
        elif choice_param == '3':
            get_folders_list(access_token)
            print()
            folder_id = int(input(colored("Enter folder Id from which you want to delete file: ", 'red')))
            print()
            get_files_in_folders(access_token,folder_id)
            print()
            file_id = int(input(colored("Enter file Id which you want to delete: ", 'red')))
            delete_file(access_token,folder_id,file_id)
             
        
    else:
        exit(101)
else:
    exit(101)
        
    
    
    


# # Get User Creds
# username = input('Enter Username: ')
# password = getpass.getpass(prompt='Enter Passowrd: ')

# user_details = {
#     'username': username,
#     'password': password
# }
# access_token = get_token(user_details)
# get_folders_list(access_token)


# # folder = input('Enter Subfolder ID: ')
# # get_files_in_folders(access_token,folder)




# # create_folder(access_token,payload)
# cprint("Note: all files under this will be deleted.", 'red')
# folder_to_delete = input('Enter Subfolder ID: ')
# delete_folder(access_token, folder_to_delete)