import requests


id = "you ID"
json_list = {}
r = requests.put('https://json.extendsclass.com/bin/{id}', headers={
      'Security-key': 'Security key',
  }, data=str(json_list).replace("'", '"').encode("utf-8"))
