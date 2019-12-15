# -*- coding: utf-8 -*-

import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
import re
#import demjson
from toutiao_config import *
import pymongo
import os
from hashlib import md5
from multiprocessing import Pool
from json.decoder import JSONDecodeError

client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

def get_page_index(offset, keyword):
    
    data = {
            'offset': offset,
            'format': 'json',
            'keyword': keyword,
            'autoload': 'true',
            'count': '20',
            'en_qc': '1',
            'cur_tab': '1'
            }

    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(data)
    # urlencode 把字典对象转化为 url请求参数
    try:
        response = requests.get(url, headers = header)
#        print(response.status_code)
        if response.status_code == 200:
            return response.text
        return None
    
    except RequestException:
        print('请求索引页出错！')
        return None

def parse_page_index(html):
    try:
        data = json.loads(html)
    #    print(type(data))
        # 用json.loads 将json字符串转换为json变量
    #    count = 0
        if data and 'data' in data.keys():
            for item in data.get('data'):
    #            count=count+1
    #            print(count, ':')
    #            print(item.get('has_gallery'))
                if item.get('article_url') != None and item.get('has_gallery') == True:
                    yield item.get('article_url')
    # has_gallery: false
    except JSONDecodeError:
        pass
                
def get_page_datail(url):
    
    try:
        response = requests.get(url, headers = header)
#        print(response.status_code)
        if response.status_code == 200:
            return response.text
        return '请求请求详情页失败！'
    
    except RequestException:
        print('请求详情页出错！')
        return None

def parse_page_datail(html,url):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    images_pattern = re.compile('gallery: JSON.parse\("(.*?)"\),',re.S)
    result = re.search(images_pattern, html)
#    print(result)
# =============================================================================
#     if result:
# #        json_result = demjson.decode(result.group(1))
# #        print(json_result)
# #        data = json_result
#         data = json.loads(result.group(1))
#         print(type(data))
#         print(data)
#         if data and 'sub_images' in data.keys():
#             sub_images = data.get('sub_images')
#             images = [item.get('url') for item in sub_images]
#             return {
#                     'title': title,
#                     'url': url,
#                     'images': images
#                     }
#     else:
#         print("没找到gallery")
# =============================================================================
    if result:
        data = result.group(1)
#        data = str(data)
#        print(data)
        pattern = re.compile('url\\\\":\\\\"(.*?)\\\\"',re.S)
        images = re.findall(pattern, data)
#        print(images)
        for image in images: download_image(image)
        return {
                    'title': title,
                    'url': url,
                    'images': images
                    }
    else:
        return '没找到gallery'
        
def save_to_mongo(result):
    
    if db[MONGO_TABLE].insert(result):
        print('存储到MongoDB成功！', result)
        return True
    return False

def download_image(url):
    
    print("当前正在下载", url)
    try:
        response = requests.get(url, headers = header)
#        print(response.status_code)
        if response.status_code == 200:
            return response.text
        return '请求图片页失败！'
    
    except RequestException:
        print('请求图片出错！', url)
        return None
    
def save_image(content):
    
    file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest, 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()
    

def main(offset):
    html = get_page_index(offset, KEYWORD)
#    with open('tupian.txt', 'w', encoding="utf-8") as f:
#        f.write(json.dumps(html, ensure_ascii=False) + '\n')
#        f.close()
        
    for url in parse_page_index(html):
        print(url)
        html = get_page_datail(url)
        if html:
            result = parse_page_datail(html, url)
            # 这个结果里还有一些意外的字符需再进行替换
            
#            print(result)
            if result: save_to_mongo(result) 
#    print(html)
    

if __name__ == '__main__':
    main()
    groups = [x*20 for x in range(GROUP_START,GROUOP_END+1)]
    pool = Pool()
    pool.map(main, groups)









