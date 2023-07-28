import os
try:
	import webbrowser
except:
	os.system('pip install webbrowser')
	import webbrowser
try:
	import requests
except:
	os.system('pip install py')
	import requests
try:
	import pyfiglet
except:
	os.system('pip install pyfiglet')
	import pyfiglet
import requests
import pyfiglet
import webbrowser
B = '\033[2;36m'#س
Z = '\033[1;31m' #احمر
h ='\033[1;101m\033[1;32m'
nam = 'rest'
print(f'{Z}'+pyfiglet.figlet_format(nam,font='big'))
def Reset():
	try:url="https://i.instagram.com/api/v1/accounts/send_password_reset/";headers={"Cookie": "mid=YxfCAQABAAG82m8NRgdsiWEYbhTq; csrftoken=8Ot6Srxbp23reyVuew7mytfMEGFoVrlC","User-Agent": "Instagram 136.0.0.34.124 Android (23/6.0.1; 640dpi; 1440x2392; LGE/lge; RS988; h1; h1; en_US)"};data={"user_id":requests.get(url="https://i.instagram.com/api/v1/users/web_profile_info/?username="+input(f"{h}Input User the account  > "),headers={"x-ig-app-id":"1217981644879628"}).json()["data"]["user"]["id"]};request=requests.post(url=url,headers=headers,data=data).json()["obfuscated_email"];return f"\033[1;32mDone Reset  \033[1;30m{request}"
	except:return "\033[1;34m اليوزر محضور"
while True:print(Reset())

#خرة بحياتي 💔
