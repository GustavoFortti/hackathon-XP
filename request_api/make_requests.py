from get_token import GetToken
import requests
import json

class MakeRequests:
	def __init__(self, token, credentials):
		self.credentials = credentials
		self.base_url = "https://openapi.xpi.com.br/openbanking"
		self.headers = {
			"Content-type": "application/json",
			"Authorization": f"Bearer {token}",
			'User-Agent': 'PostmanRuntime/7.26.8'
		}

	def try_request(self, req, **params):
		res = req(**params)
		if res.status_code == 401:
			token= GetToken(self.credentials["client_id"], self.credentials["client_secret"]).access_token
			self.headers["Authorization"] = f"Bearer {token}"
			res = req(*params)
			return res
		return res
		

	def users(self, user_name=None):
		url = self.base_url + f'/users/{user_name}'
		print("URL =>", url)
		resp = requests.get(url, headers=self.headers)
		return resp
	
	def user_investments(self, bank=None, user_name=None):
		print(bank)
		print(user_name)
		url = self.base_url + f"/bank/{bank}/users/{user_name}/investments"
		print("URL =>", url)
		resp = requests.get(url, headers=self.headers)
		return resp

