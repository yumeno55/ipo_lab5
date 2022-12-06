import json

import requests
from config import TOKEN


def get_response(num):
    global response
    data = {'name': repoName,
            'homepage': 'https://github.com',
            'private': False,
            'is_template': True}
    headers = {'Content-type': 'application/json',
               "Authorization": f"Bearer {token}"}
    match num:
        case 1:
            response = requests.get(f"https://api.github.com/orgs/{orgName}/repos", params={"per_page": 3})
        case 2:
            response = requests.get(f"https://api.github.com/user/repos", params={"visibility": "public"},
                                    headers={"Authorization": f"Bearer {token}"})
        case 3:
            response = requests.post(f"https://api.github.com/user/repos", data=json.dumps(data),  headers=headers)
        case 4:
            response = requests.delete(f"https://api.github.com/repos/{userName}/{repoName}",
                                       headers={"Authorization": f"Bearer {token}"})

    print(f"Status code: {response.status_code}")
    print(f"Response body: {response.text}")


if __name__ == '__main__':
    orgName = "Microsoft"
    userName = "yumeno55"
    repoName = "Repo2"
    token = TOKEN
    get_response(4)
