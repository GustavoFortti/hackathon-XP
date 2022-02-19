import requests
from requests.structures import CaseInsensitiveDict
import json

def gen_token():
    url = "https://openapi.xpi.com.br/oauth2/v1/access-token"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["User-Agent"] = "PostmanRuntime/7.26.8"

    data = "grant_type=client_credentials&client_id=K47RigTncvJCEc6XwyxACWfL8DYOoXcFuMtXM9AFsSDs8GFO&client_secret=ERL0P2OlMT6s5aGooxVAuRdme3MG1jeyA75xyNayGiLwAHmy9kCeehs9q9a5zmPp"
    resp = requests.post(url, headers=headers, data=data)

    return resp.json()['access_token']

def get_data(url: str):
    token = read_token()
    res = request_data(url, token)

    if (res.status_code == 401):
        token = gen_token()
        print(token)
        res = request_data(url, token)
        write_token(token)

    return res        

def request_data(url: str, token: str):
    headers = CaseInsensitiveDict()
    headers["Content-type"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"
    headers["User-Agent"] = "PostmanRuntime/7.26.8"

    return requests.get(url, headers=headers)

def read_token():
    f = open('auth.json')
    token = json.load(f)['token']
    f.close()
    return token

def write_token(token: str):
    dictionary = {
        'token': token
    }
    
    with open("auth.json", "w") as outfile:
        json.dump(dictionary, outfile)