import requests
import json

id = 'you ID'
r = requests.get(f'https://json.extendsclass.com/bin/{id}', headers={
	'Security-key': 'security key'
})

json_list = json.loads(r.text)
