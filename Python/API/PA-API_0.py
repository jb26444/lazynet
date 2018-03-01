import requests

url = "https://10.116.26.167/api/"

querystring = {"type":"keygen","user":"admin","password":"AnimalAcc3ss"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "0054d7b6-4b91-51e1-edc2-b814d5b5b915"
    }

response = requests.request("GET", url, verify=False, headers=headers, params=querystring)

print(response.text)
