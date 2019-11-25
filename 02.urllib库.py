# -*- coding: utf-8 -*-


# https://yiyibooks.cn/xx/python_352/library/urllib.request.html#urllib.request.urlopen
# urllib.request.urlopen(url, data=None, [timeout, ]*, ...)
import urllib.request
# GET请求百度页面
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))
# read() 是以字节流读取，decode() 转换格式

# =============================================================================\
# POST形式发送请求,要有data参数
import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'world':'hello'}),encoding = 'utf-8')
response = urllib.request.urlopen('http://www.httpbin.org/post',data = data)
# http://www.httpbin.org/  常用来做http测试
print(response.read())

# =============================================================================
import socket
import urllib.request
import urllib.error

try:
    respone = urllib.request.urlopen('http://www.httpbin.org/get',timeout=0.1)
    # 限定请求时长
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
#      isinstance(object, classinfo) 如果object是clsaainfo的一个实例,则返回true,详情>>https://yiyibooks.cn/xx/python_352/library/functions.html#isinstance
#       e.reason 返回HTTP错误原因 print(e.reason)
        print('TIME OUT')


# =============================================================================
# 响应
import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
# 响应类型
print('响应类型:',type(response))
# 响应代码
print('响应代码:',response.status)
# 响应头
print('响应头:\n',response.getheaders())
print('响应头Server:',response.getheader('Server'))


# =============================================================================
# Request
# 1. request 只传一个参数URL
import urllib.request

request = urllib.request.Request('http://www.baidu.com')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

# =============================================================================
# 2. 参数比较多时分开写
from urllib import request,parse

url = 'http://www.baidu.com'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Host': 'www.baidu.com'
        }
dict = {'name': 'BOb'}
data = bytes(parse.urlencode(dict),encoding='utf8')
req = request.Request(url=url,data=data,headers=headers,method='POST')

req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')
# add_header(key,value) 向之前的headers中追加参数键值对，键值冲突时以最新的替代

response = request.urlopen(req)
print(response.read().decode('utf-8'))

# =============================================================================
# Handler 代理
import urllib.request

proxy_headler = urllib.request.ProxyHandler({
        'http':'http://183.3.218.34:8080',
        'https':'https://183.3.218.34:8080'
        })
opener = urllib.request.build_opener(proxy_headler)
response = opener.open('http://httpbin.org/get')

print(response.read().decode('utf8'))


# =============================================================================
# Cookie 维持登录信息，登录状态
import http.cookiejar,urllib.request

cookie = http.cookiejar.CookieJar()
headler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(headler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)

# - 保存cookie信息到本地文件
import http.cookiejar,urllib.request
filename = "cookie.txt"
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(headler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)

# 另外一种保存格式/方法
import http.cookiejar,urllib.request
filename = "cookie.txt"
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(headler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)

# LWP形式读取本地Cookie信息
import http.cookiejar,urllib.request

cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
headler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(headler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))


# =============================================================================
# 异常处理
# 1.小例子
from urllib import request,error

try:
    response = request.urlopen('http://cuiqingcai.com/index.html')
except error.URLError as e:
    print(e.reason)

# 2.一般捕获异常顺序
from urllib import request,error

try:
    response = request.urlopen('http://cuiqingcai.com/index.html')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
    # sep控制每个字符之间的字符，默认为一个空格
except error.URLError as e:
    print(e.reason)
else:
    print('Request Scueessfully')

# 3.
import socket
import urllib.request
import urllib.error

try:
    respone = urllib.request.urlopen('http://www.httpbin.org/get',timeout=0.1)
    # 限定请求时长
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')

# =============================================================================
# urlparse 解析URL
# - urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
#   参数:scheme指定协议类型，如果url中有协议字段，以URL中的协议为准，忽略此参数
#        allow_fragments 布尔值是否忽略fragments的值
from urllib.parse import urlparse
result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result,sep='\n')

from urllib.parse import urlparse
result = urlparse('https://www.baidu.com/index.html;user?id=5#comment',scheme='http')
print(type(result),result,sep='\n')

from urllib.parse import urlparse
result1 = urlparse('https://www.baidu.com/index.html;user?id=5#comment',allow_fragments=True)
print(type(result1),result1,sep='\n')

result2 = urlparse('https://www.baidu.com/index.html;user?id=5#comment',allow_fragments=False)
print(type(result2),result2,sep='\n')

result3 = urlparse('https://www.baidu.com/index.html#comment',allow_fragments=False)
print(type(result3),result3,sep='\n')

# =============================================================================
# urlunparse 用来拼接URL
# - tip:按顺序拼接
from urllib.parse import urlunparse

data = ['http','www.baidu.com','index.html','user','a=6','comment']
# data = ('http','www.baidu.com','index.html','user','a=6','comment') # 也OK
print(urlunparse(data))

# =============================================================================
# urljoin 
from urllib.parse import urljoin
print(urljoin('http://www.baidu.com','FAQ.html'))
print(urljoin('http://www.baidu.com/index.html','http://www.baidu.com'))
print(urljoin('http://www.baidu.com/index.html','http://www.baidu.com/FAQ.html'))
print(urljoin('http://www.baidu.com?id=5','http://www.baidu.com/FAQ.html'))
print(urljoin('http://www.baidu.com','?id=5#comment'))
print(urljoin('http://www.baidu.com#comment','?id=5'))

# =============================================================================
# urlencode 把字典对象转化为get请求的参数
from urllib.parse import urlencode

params = {'name':'germey','age':'18'}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)


