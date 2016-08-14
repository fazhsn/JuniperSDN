'''
This class generates the Authentication Header which can be used with any program
'''


import requests
requests.packages.urllib3.disable_warnings()
import json



class Auth():

	def Authheader(self):
		url = "https://10.10.2.29:8443/oauth2/token"

		payload = {'grant_type': 'password', 'username': 'group1', 'password': 'Group1'}
		response = requests.post (url, data=payload, auth=('group1','Group1'), verify=False)
		json_data = json.loads(response.text)
		authHeader= {"Authorization":"{token_type} {access_token}".format(**json_data)}
		return authHeader

