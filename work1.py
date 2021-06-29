import requests
import json,time,datetime

from requests.api import request

from requests.models import Response
from requests.sessions import session



datetimename = datetime.datetime.today().strftime("%Y%m%d%H%M%S")

url = "http://tsukumonet.ddns.net:21126/login"
signurl = "http://tsukumonet.ddns.net:21126/signup"
changenameurl = 'http://tsukumonet.ddns.net:21126/post_userNick'

headers = {'Content-Type': "application/json",
           'Host': "tsukumonet.ddns.net:21126",
           'Origin': "http://tsukumonet.ddns.net:21126",
           'Referer': "http://tsukumonet.ddns.net:21126/login",
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",}

headers2 = {'Content-Type': "application/json",
           'Host': "tsukumonet.ddns.net:21126",
           'Origin': "http://tsukumonet.ddns.net:21126",
           'Referer': "http://tsukumonet.ddns.net:21126/signup",
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",}

headers3 = {'Content-Type': "application/json",
           'Host': "tsukumonet.ddns.net:21126",
           'Origin': "http://tsukumonet.ddns.net:21126",
           'Referer': "http://tsukumonet.ddns.net:21126/index",
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",}

session = requests.session()

def sign(newuserid,newuserpa,newname):
    sign = {'account':newuserid,
            'name':newname,
            'password':newuserpa,
            
            }
    response = requests.post(url = signurl , data = json.dumps(sign),headers=headers2)
    print(response.text)
    if(response.text == '{"status":"ERROR","msg":"This account is exists"}'):
        print('帳號已經使用過囉')
        print('newid')
        newuserid = input()
        print('newpassword')
        newuserpassword = input()
        print('name')
        newname = input()
        sign(newuserid,newuserpassword,newname)
    print('成功')

def login(userid,userpa):    
    payload = {'account': userid,
                'password': userpa,
            }
    response = session.post(url = url,data = json.dumps(payload),headers = headers)
    print(response.text)
    if(response.text=='{"status":"ERROR","msg":"This account not exists"}' or response.text == '{"status":"ERROR","msg":"Wrong password"}'):
        print('帳號或密碼錯誤我也不知道哪一個錯,辦帳號Y/N')
        chickans = input()
        if(chickans == 'N'):
            print('正確帳號')
            chickid = input()
            print('正確密碼') 
            chickpassword = input()
            login(chickid,chickpassword)
        elif(chickans == 'Y'):
            print('newid')
            newuserid = input()
            print('newpassword')
            newuserpassword = input()
            print('name')
            newname = input()
            sign(newuserid,newuserpassword,newname)
            print('辦理帳號中')
            time.sleep(2)
            login(newuserid,newuserpassword)

def changename(datetimename):
    changename = {
        'userNick' : '我的名字'+datetimename,
    }
    response = session.post(url = changenameurl , data = json.dumps(changename),headers = headers)
    print(response.text)


print('是否持有帳號密碼Y/N')
ans = input()
if(ans=='Y'):
    print('ID')
    userid = input()
    print('password')
    userpa = input()
    login(userid,userpa)
elif(ans=='N'):
    print('newid')
    newuserid = input()
    print('newpassword')
    newuserpassword = input()
    print('name')
    newname = input()
    sign(newuserid,newuserpassword,newname)
    print('辦理帳號中')
    time.sleep(2)
    login(newuserid,newuserpassword)
 

changename(datetimename)



