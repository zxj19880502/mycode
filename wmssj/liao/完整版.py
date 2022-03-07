# -*- coding: utf8 -*-
from play import playsound
from aip import AipSpeech
import requests
""" 你的 APPID AK SK """
APP_ID = '25696097'
API_KEY = 'mbDDrMlNOxvzPixxQr6piuDf'
SECRET_KEY = 'WSEnOvuPeDhneuuCmGHyWwCFQGBUtwEt'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

print('请输入你想说的：')

while True:
    a=input()
    url='https://api.ownthink.com/bot?appid=c5e635b0bd92140a1f736fe89b10042d&spoken=%s'%a
    te=requests.get(url).json()
    data=te['data']['info']['text']
    print(data)
    result = client.synthesis(data, 'zh', 1, {
        'vol': 8,  # 音量
        'spd': 5,  # 语速
        'pit': 9,  # 语调
        'per': 4,  # 0：女 1：男 3：逍遥 4：小萝莉
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb+',errors='ignore') as f:
            f.write(result) 

    p = playsound()
    voice_path = r"auido.mp3"
    p.play(voice_path)  # 播放
    p.close()  # 停止
