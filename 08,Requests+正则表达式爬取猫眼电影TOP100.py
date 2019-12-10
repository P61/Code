# -*- coding: utf-8 -*-

import requests
from requests.exceptions import RequestException
import re

def get_one_page(url):
    '''
        获得网页代码
    '''    
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    try:
        response = requests.get(url, headers = header)
#        print(response.text)
#        print(response.status_code)
        if response.status_code ==200 :
            return response.text
        else:
            return None
    except RequestException:
        return None

def Re(string):
    '''
        用正则匹配出有用的信息
    '''
#    filmname = []
#    temp1 = re.findall('<p class="name"><a.*?>(.*?)</a></p>',string,re.S)
#    filmname.append(temp1)
    filmname = re.findall('<p class="name"><a.*?>(.*?)</a></p>',string,re.S)
    star = re.findall('<p class="star">\n.*?主演：(.*?)\n.*?</p>',string,re.S)
    releasetime = re.findall('<p class="releasetime">上映时间：(.*?)</p>',string,re.S)
    print(filmname)
    print(star)
    print(releasetime)
# <li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>

def Write(string):
    '''
        写入本地
    '''
    with open('HTML.html', 'w', encoding="utf8") as HTML:
        HTML.write(string)


def main():
    url = 'https://maoyan.com/board/4'
    html = get_one_page(url)
    Re(html)
#    print(html)
#    Write(html)

if __name__=='__main__':
    main()

    
    
    