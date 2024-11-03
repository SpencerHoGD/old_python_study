
# -*- coding: utf-8 -*-

#author:hexiaoming



from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '16721665'
API_KEY = 'hDVha4SRKUBI3Vhue85Rm5me'
SECRET_KEY = 'SBbPI9PT0WS8L48fXCZNXxEktrIP6lVa'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

filePath = "images/001.jpg"



""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(filePath)

#""" 调用通用文字识别, 图片参数为本地图片 """
#client.basicGeneral(image);

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
#options["detect_language"] = "true"
#options["probability"] = "true"

#""" 带参数调用通用文字识别, 图片参数为本地图片 """
#result = client.basicGeneral(image, options)


""" 带参数调用通用文字识别（高精度版） """
result = client.basicAccurate(image, options)


""" 将返回的result写入txt文件str """
with open(f'{filePath}.txt', 'wb') as f:
        f.write(str(result).encode('utf-8'))

#url = "http//www.x.com/sample.jpg"

#""" 调用通用文字识别, 图片参数为远程url图片 """
#client.basicGeneralUrl(url);

#""" 如果有可选参数 """
#options = {}
#options["language_type"] = "CHN_ENG"
#options["detect_direction"] = "true"
#options["detect_language"] = "true"
#options["probability"] = "true"

#""" 带参数调用通用文字识别, 图片参数为远程url图片 """
#client.basicGeneralUrl(url, options)