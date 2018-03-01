import requests

url = "https://10.116.26.167//api/"

querystring = {"type":"op","cmd":"<show><system><info></info></system></show>","key":"LUFRPT1sQUx6V0swNE9wc3U5RkVVN3g4Q09IemI0NVE9dVpjS0l6dVVtSCtKSzNGWEM5UUZieVJ2NXBqeFg3Y29zeVZBeTJhb0pkMD0="}

headers = {
    'cache-control': "no-cache",
    'postman-token': "a903d0d4-a81b-ca4e-9310-993eeba2e6c7"
    }

response = requests.request("GET", url, verify=False, headers=headers, params=querystring)

print(response.text)
