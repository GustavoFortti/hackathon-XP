
import requests
import json

class GetToken:
    def __init__(self, client_id, client_secret):
        self.access_token = None
        self.url = 'https://openapi.xpi.com.br/oauth2/v1/access-token'
        self.body = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'PostmanRuntime/7.26.8'
        }
        self.get_access_token()

    def get_access_token(self):
        try:
          resp = requests.post(self.url, data=self.body, headers=self.headers)
          self.access_token = json.loads(resp.text)["access_token"]
        except Exception as e:
          print("Exception =>", e)
          print(e.with_traceback.__annotations__)
          print(Exception.with_traceback)
