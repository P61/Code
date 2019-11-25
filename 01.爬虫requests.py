import requests


response = requests.get('http://www.baidu.com')
response.encoding='utf-8'
print(response.text)
print(response.headers)
print(response.status_code)

