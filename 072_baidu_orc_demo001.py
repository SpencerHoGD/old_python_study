# -*- coding: utf-8 -*-

#author:hanshiqiang365 （微信公众号：韩思工作室）    
# https://github.com/hanshiqiang365/baidu_demo/blob/master/baidu_ocr_demo/


from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '16721665'
API_KEY = 'hDVha4SRKUBI3Vhue85Rm5me'
SECRET_KEY = 'SBbPI9PT0WS8L48fXCZNXxEktrIP6lVa'

aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

filePath = "images/001.jpg"

# 读取图片

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 定义参数变量
options = {
  'detect_direction': 'true',
#  'language_type': 'ENG+JPN',
}

# 调用通用文字识别接口
result = aipOcr.basicAccurate(get_file_content(filePath), options)

#print(result)

with open(f'{filePath}.txt', 'wb') as f:
    f.write(str(result).encode('utf-8'))