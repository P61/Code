# -*- coding: utf-8 -*-

import requests

response = requests.get('https://www.baidu.com/')
print('response类型：',type(response))
print('状态码：',response.status_code)
print('response.text返回类型：',type(response.text))
print('返回内容：',response.text)
print('cookie信息：',response.cookies)





















