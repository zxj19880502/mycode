# coding=gbk
"""
作者：川川
时间：2021/8/22
私人交流群：970353786
"""
# pip install baidu-aip
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '25696097'
API_KEY = 'mbDDrMlNOxvzPixxQr6piuDf'
SECRET_KEY = 'WSEnOvuPeDhneuuCmGHyWwCFQGBUtwEt'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result = client.synthesis('空山新雨后，天气晚来秋', 'zh', 1, {
    'vol': 5,  # 音量
    'spd': 3,  # 语速
    'pit': 9,  # 语调
    'per': 3,  # 0：女 1：男 3：逍遥 4：小萝莉
})
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)
