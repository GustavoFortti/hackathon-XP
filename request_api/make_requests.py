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

	def try_request(self, req, *params):
		res = req(*params)
		if res.status_code == 401:
			token= GetToken(self.credentials["client_id"], self.credentials["client_secret"]).access_token
			self.headers["Authorization"] = f"Bearer {token}"
			res = req(*params)
			return res
		return res
		

	def users(self, limit=None, offset=None):

		if limit:
			url = self.base_url + f'/users/?limit={limit}'
		elif offset:
			url = self.base_url + f'/users/?limit={limit}&offset={offset}'
		else:
			url = self.base_url + '/users/'

		resp = requests.get(url, headers=self.headers)

		return resp