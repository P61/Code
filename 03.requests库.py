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
# 请求
## 基本GET请求
#  - 基本写法
import requests

response = requests.get('http://httpbin.org/get')
print(response.text)


#  - 带参数GET请求
import requests

response = requests.get('http://httpbin.org/get?name=BOb&age=22')
print(response.text)


import requests

data = {'name':'Levine','age':18}
response = requests.get('http://httpbin.org/get',params=data)
print(response.text)

# =============================================================================
#  - 解析json 
import requests

requests = requests.get('http://httpbin.org/get')
print(type(response.text))
print(response.json())
print(type(response.json()))
# response.text返回字符串
# response.json()返回字典(json字符串)

# =============================================================================
#  - 获取二进制数据
import requests

response = requests.get('https://github.com/favicon.ico')
print(type(response.text))
print(type(response.content))# <class 'bytes'>
print(response.text)
print(response.content)

#  - 保存到本地
import requests

response = requests.get('https://github.com/favicon.ico')
with open('favicon.ico','wb') as f:
    f.write(response.content)
    f.close()
# =============================================================================
#  - 添加headers
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

response = requests.get('https://www.zhihu.com/explore', headers=headers)
print(response.text)

# =============================================================================
# 基本的POST请求
import requests

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

data = {'name':'Levine','age':'18'}
response = requests.post('http://httpbin.org/post',data=data)
print(response.text)

# =============================================================================
# 响应
#  - response属性
import requests

response = requests.get('https://www.baidu.com/')
print('状态码：',type(response.status_code),response.status_code)
print('headers：',type(response.headers),response.headers)
print('cookies：',type(response.cookies),response.cookies)
print('url：',type(response.url),response.url)
print('history：',type(response.history),response.history)


# 状态码的判断
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

response = requests.get('https://www.jianshu.com/',headers=headers)
#print(response.status_code)
#print(response.text)
if response.status_code == requests.codes.ok:
    print('Request Successfully')
else:
    print('Request fail')


# =============================================================================
# 高级操作
import requests

files = {'file': open('favicon.ico','rb')}
response = requests.post('http://httpbin.org/post',files= files)
print(response.text)

# =============================================================================
# 获取cookies
import requests

response = requests.get('https://www.baidu.com/')
print(response.cookies)
for key,value in response.cookies.items():
    print(key +'='+ value)

# =============================================================================
# 会话维持
import requests

requests.get('http://httpbin.org/cookies/set/number/123456789')
response = requests.get('http://httpbin.org/cookies')
print(response.text)


import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response = s.get('http://httpbin.org/cookies')
print(response.text)

# =============================================================================
# 证书验证
import requests

response = requests.get('https://www.12306.cn')
print(response.status_code)

import requests
from requests.packages import urllib3 # 不验证证书会报警告信息
urllib3.disable_warnings()            # 引入此包不会报警告信息
response = requests.get('https://www.12306.cn',verify=False) # verify是否验证证书参数
print(response.status_code)


# 引用本地证书
import requests

response = requests.get('https://www.12306.cn',cert=('/path/server.crt','/path/key'))
# cert文件夹路径
print(response.status_code)


# =============================================================================
# 代理设置
import requests

proxies = {"http":"http://121.199.36.121:3128",
           "https":"https://121.199.36.121:3128"}

response = requests.get("https://www.taobao.com",proxies=proxies)
print(response.status_code)

# 需要密码的代理
import requests

proxies = {"http":"http://user:password@121.199.36.121:3128",
           "https":"https://user:password@121.199.36.121:3128"}

response = requests.get("https://www.taobao.com",proxies=proxies)
print(response.status_code)

# =============================================================================
# 超时设置 和异常捕获
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException
try:
    response = requests.get("https://www.httpbin.org/get",timeout=1)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
except HTTPError:
    print('Http error')
except RequestException:
    print('Error')
    
# =============================================================================
# 认证设置(登录验证)
import requests
from requests.auth import HTTPBasicAuth

r = requests.get('http://121.199.36.121:3128',auth=HTTPBasicAuth('user','123'))
print(r.status_code)


import requests

r = requests.get('http://121.199.36.121:3128',auth=('user','123'))
print(r.status_code)












