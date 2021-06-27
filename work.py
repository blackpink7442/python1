
import requests


username = 'a1'
userpass = 'a1'
url = 'http://tsukumonet.ddns.net:21126/login'

session_requests = requests.Session()

headers = {
    'Host' : 'tsukumonet.ddns.net:21126',
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Accept-Encoding' : 'gzip, deflate',
    'Accept':'*/*',
    'Connenction' : 'keep-alive',
}

login ={
    "account" : "a1",
    "password": "a1",
    
}
result = session_requests.get(url)

result=session_requests.post(url,headers=headers,data = login)

result = session_requests.get('http://tsukumonet.ddns.net:21126/index',headers=headers)
print(result.status_code)
print(result.text)
print(result.url)
