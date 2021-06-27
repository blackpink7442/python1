import requests
import json
url = "http://tsukumonet.ddns.net:21126/login"




userid = "a1"
userpa = "a1"


headers = {'Content-Type': "application/json",
           'Host': "tsukumonet.ddns.net:21126",
           'Origin': "http://tsukumonet.ddns.net:21126",
           'Referer': "http://tsukumonet.ddns.net:21126/login",
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",}

payload = {'account': userid,
           'password': userpa,
           }

response = requests.post(url = url,data = json.dumps(payload),headers = headers)
print(response.text)
print(response.url)
