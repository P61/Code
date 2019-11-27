# -*- coding: utf-8 -*-
import random

import requests

import pymongo


url_for_test = 'http://httpbin.org/ip'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}

def get_random_ip():

    '''

    随机取出一个ip

    '''

    client = pymongo.MongoClient(host='localhost',port=27017)

    db = client.PROXY

    collection = db.proxies

    items = collection.find()

    length = items.count()

    ind = random.randint(0,length-1)

    useful_proxy = items[ind]['ip'].replace('\n','')

    proxy = {

        'http': 'http://' + useful_proxy,

        'https': 'http://' + useful_proxy,

        }   

    response = requests.get(url_for_test,headers=headers,proxies=proxy,timeout=10)

    if response.status_code == 200:

        return useful_proxy

    else:

        print('此{ip}已失效'.format(useful_proxy))

        collection.remove(useful_proxy)

        print('已经从MongoDB移除')

        get_random_ip()
        
        
if __name__ == '__main__':
    
    finally_ip = get_random_ip()

    print('取出的ip为：' + finally_ip)
    
