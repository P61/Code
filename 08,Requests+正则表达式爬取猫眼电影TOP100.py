# -*- coding: utf-8 -*-

import requests
from requests.exceptions import RequestException
import re
import json
#from multiprocessing import Pool

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
    index = re.findall('<i class="board-index board-index-.*?">(.*?)</i>',string,re.S)
    img = re.findall('<img data-src="(.*?)"',string,re.S)
    title = re.findall('<p class="name"><a.*?>(.*?)</a></p>',string,re.S)
    star = re.findall('<p class="star">\n.*?主演：(.*?)\n.*?</p>',string,re.S)
    releasetime = re.findall('<p class="releasetime">上映时间：(.*?)</p>',string,re.S)
    score = re.findall('<i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>',string,re.S)
#    print(index)
#    print(img)
#    print(title)
#    print(star)
#    print(releasetime)
#    print(score)
    for k in range(10):
        yield {
            'index': index[k],
            'title': title[k],
            'star': star[k],
            'releasetime': releasetime[k],
            'score': score[k][0]+score[k][1],
            'image': img[k]
        }
    
#    print(scores[0]|scores[1])
# <li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>

def Write(string):
    '''
        写入本地
    '''
    with open('result.txt', 'a', encoding="utf-8") as f:
        f.write(json.dumps(string, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in Re(html):
        print(item)
        Write(item)

if __name__=='__main__':
    for k in range(10):
        main(k*10)
#    pool = Pool()
#    pool.map(main, [i*10 for i in range(10)])
#    使用多线程会出现同时写入问题，顺序会不一样，并且同一个项目会被切开

    