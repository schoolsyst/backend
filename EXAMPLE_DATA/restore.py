#!/usr/bin/python3
import json
import os
import sys
import re
import requests
from inquirer import Checkbox, prompt, Confirm

BASE_URL = "http://localhost:9999/api/"
TOKEN_URL = BASE_URL + 'auth/'
DETAILED_LOGS = False
FILES = [  # In dependency order.
    'subjects.json', 'settings-definitions.json', 'settings.json', 'events.json', 'notes.json'
]
DISTANT_VALUE_REGEX = re.compile(r'@(?P<endpoint>[^.]+)\.(?P<get_prop>[^:]+):(?P<search_in_prop>[^=]+)=(?P<search_for>.+)')

def get_token(username=None, password=None, endpoint=TOKEN_URL):
    user = username or input('Username: ')
    if user and not password: print(f'Username: {user}')
    pwrd = password or input('Password: ')
    try:
        token = requests.post(endpoint, data={
            'username': user,
            'password': pwrd
        }).json()['token']
    except KeyError:
        print('Invalid admin credentials. Prompting for credentials...')
        return get_token(None, None)
    print(f'Got token: {token:.30}{"…" if len(token) > 30 else ""}')
    return token


def delete_all(table, token):
    print(f'DELETING ALL CURRENT DATA FOR {table}...')
    resp = requests.get(f'{BASE_URL}{name}/', headers={'Authorization': f'Bearer {token}'})
    uuids = [item['uuid'] for item in json.loads(resp.content)]
    for uuid in uuids:
        print(f'    Deleting {name} item with UUID "{uuid}"...')
        res = requests.delete(f'{BASE_URL}{name}/{uuid}', headers={'Authorization': f'Bearer {token}'})
        print(f'        Got {res.status_code} response.')
def load_data(filename):
    print(f'Getting data from {filename}...')
    with open(filename, 'r', encoding="utf8") as file:
        return json.loads(file.read())

def get_server_data(endpoint, token, base_url=BASE_URL):
    url = base_url + endpoint
    return requests.get(url, headers={'Authorization': f'Bearer {token}'}).json()

def get_distant_value(endpoint, get_prop, search_in_prop, search_for, token):
    # Example:
    # @subjects.uuid:slug=histoire-geographie
    #   |        |     |           |
    #   |        |     |           | search_for
    #   |        |     | search_in_prop
    #   |        | get_prop
    #   | endpoint
    #
    # will make a request to (BASE_URL + 'subjects') and
    # return the 'uuid' for a subject whose 'slug' equals 'histoire-geographie'
    #
    # Returns a tuple: (status, error_message if not status else found_value)
    objects = get_server_data(endpoint, token)
    found = None
    # Search through each object
    for obj in objects:
        try:
            # Get the field and test against the value
            if obj[search_in_prop] == search_for:
                # Set `found` to this object and break outta the loop
                found = obj
                break
        except KeyError:
            continue
    # If `found` is None, no object matched the condition
    if found is None:
        return (False, f'No object in {endpoint} with {search_in_prop} == {search_for}')
    # Get the value from the found object
    try:
        return (True, found[get_prop])
    except KeyError:
        return (False, f'Object found has no {get_prop}')


def make_request(data, token):
    print(f'Request to {BASE_URL}{name}/ with data...')
    if DETAILED_LOGS: print(json.dumps(data, indent=2))

    for (k, v) in data.items():
        if type(v) is str and DISTANT_VALUE_REGEX.match(v):
            distant_value_params = DISTANT_VALUE_REGEX.search(v).groupdict()
            status, error_or_data = get_distant_value(**distant_value_params, token=token)
            if status:
                print(f'    Got distant value {v}')
                data[k] = error_or_data
            else:
                print(f'    Error while getting distant value "{v}": {error_or_data}')
                print(f'    Aborting POST request.')
                return

    res = requests.post(f'{BASE_URL}{name}/',
                        data=data,
                        headers={'Authorization': f'Bearer {token}'}
                       )
    print(f'    Got a {res.status_code} response with data...')
    if res.status_code not in [201, 200]: print('   '+res.text)
    if res.status_code in range(500, 599): sys.exit(f"  Got a {res.status_code} response: quitting.")

def prompt_multiple_choices(choices):
    question = Checkbox('resources', message="What to send to the database?", choices=choices)
    selected = prompt([question])['resources']
    return sorted(selected, key=choices.index)



if __name__ == "__main__":
    # capture cwd to restore at the end & cd to correct dir
    cwd = os.getcwd()
    os.chdir(os.path.dirname(__file__))
    # Get token. note: these credentials are local-only.
    token = get_token('ewen-le-bihan', '^bXq2##7*ev8*4i%3$LGKzvd$HdN$')
    # Destroy db or keep it ?
    reset = prompt([Confirm('reset', message='Replace current data', default=False)])['reset']
    # Restore each .json file
    for file in prompt_multiple_choices(FILES):
        if file.endswith('.json'):
            name = file.replace('.json', '')
            data = load_data(file)
            if reset: delete_all(name, token)
            for item in data:
                make_request(item, token)
    # Restore the cwd
    os.chdir(cwd)
