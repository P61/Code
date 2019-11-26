# -*- coding: utf-8 -*-

# requests 实例
import requests

response = requests.get('https://www.baidu.com/')
print('response类型：',type(response))
print('状态码：',response.status_code)
print('response.text返回类型：',type(response.text))
print('返回内容：',response.text)
print('cookie信息：',response.cookies)

# =============================================================================
# 各种请求方式
import requests
requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/get')
requests.options('http://httpbin.org/get')




# =============================================================================



















