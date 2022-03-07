import requests
import pyttsx3
print("你想对我说什么？：")

while True:
    a=input()
    url='https://api.ownthink.com/bot?appid=c5e635b0bd92140a1f736fe89b10042d&spoken=%s'%a
    te=requests.get(url).json()
    data=te['data']['info']['text']
    print(data)
    ini= pyttsx3.init()
    shuo=ini.say(data)
    ini.runAndWait()