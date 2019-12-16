# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from pyquery import PyQuery as pq
import pymongo

MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_TABLE = 'product'

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


browser = webdriver.Chrome()
#browser = webdriver.PhantomJS()
#browser.set_window_size(1400,900)
# 自己想可以尝试用PhantomJS使用cookies，解决登陆问题
# https://phantomjs.org/api/command-line.html

wait = WebDriverWait(browser, 10)
# = {'cookie': 'thw=cn; cna=pW1+FnHCAxACAXbNLGEGLYT0; v=0; t=058f3688fd77bc79174b2b8e2d9b0293; cookie2=195d7d0e3880b64eb76031126acadb1e; _tb_token_=e7ee47eef45e5; unb=2230102536; uc3=vt3=F8dByuqm7ZWHl9Z7hns%3D&lg2=WqG3DMC9VAQiUQ%3D%3D&id2=UUpictSnKgfkZQ%3D%3D&nk2=E6Ax585GwMz%2B; csg=626de54a; lgc=pdh521pdh; cookie17=UUpictSnKgfkZQ%3D%3D; dnk=pdh521pdh; skt=975b8941047a5c40; existShop=MTU3NjUwMTE3NA%3D%3D; uc4=nk4=0%40Ebk1L8IAXgFExgE%2BZpGGkslXNKg%3D&id4=0%40U2got32sFUDDMtG9SNjzPN0YMhh%2B; tracknick=pdh521pdh; _cc_=UIHiLt3xSw%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=h64; _nk_=pdh521pdh; cookie1=VFR3DhwleDy1Dbn94FjX1qcUFMlgLN8S6Be6iV6f7Io%3D; enc=vFBEA3L7G7qPsHPgcRCz8xoQLYABs%2B2dyVjsfJTqV4smSOXwrA2iHhfGChJ8hYMN8TxWlKU%2BPcbyKDgy5y98BQ%3D%3D; JSESSIONID=A19FB86DDF13907A41E8B92F60F70AB5; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=UIHiLt3xSifiVqTH8o%2F0Qw%3D%3D&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&pas=0&cookie14=UoTbm8LS9X216A%3D%3D&tag=8&lng=zh_CN; mt=ci=8_1; l=dBQnSrsnqvCoUsP2BOCwhurza77O9IRfguPzaNbMi_5CE68lnD7OkUfTGFJ6cjXATk8BqdH2-se9xut7JjJcSlvX4AadZJk2B; isg=BCoqgiT6AxKvQ49-m_zzVtWXe5DMm671BdX-9rTj630F58uhnCvuBOjVc1LeFyaN'}


def serch1():
    '''
        尝试微博登陆，没成功，可以用超级鹰的识别验证码来登陆
    '''
    try:
        browser.get('https://login.taobao.com/')
        browser.find_element_by_xpath('//*[@id="J_OtherLogin"]/a[1]').click()
        # 输入账号和密码
        browser.find_element_by_name("username").clear()
        browser.find_element_by_name("username").send_keys("18339474940")
        browser.find_element_by_name('password').clear()
        browser.find_element_by_name("password").send_keys("pdh5216919")
        browser.find_element_by_xpath('//*[@class="btn_tip"]/a/span').click()
    except:
        pass
    return 0

def search():
    print('正在搜索..')
    try:
#        browser.add_cookie({'thw': 'cn', 
#                            'cna': 'pW1+FnHCAxACAXbNLGEGLYT0', 
#                            'v': '0', 
#                            't': '058f3688fd77bc79174b2b8e2d9b0293', 
#                            'cookie2': '195d7d0e3880b64eb76031126acadb1e', 
#                            '_tb_token_': 'e7ee47eef45e5', 
#                            'unb': '2230102536', 
#                            'uc3': ['vt3', 'F8dByuqm7ZWHl9Z7hns%3D&lg2', 'WqG3DMC9VAQiUQ%3D%3D&id2', 'UUpictSnKgfkZQ%3D%3D&nk2', 'E6Ax585GwMz%2B'], 
#                            'vt3': '',
#                            'csg': '626de54a', 
#                            'lgc': 'pdh521pdh', 
#                            'cookie17': 'UUpictSnKgfkZQ%3D%3D', 
#                            'dnk': 'pdh521pdh', 
#                            'skt': '975b8941047a5c40', 
#                            'existShop': 'MTU3NjUwMTE3NA%3D%3D', 
#                            'uc4': ['nk4', '0%40Ebk1L8IAXgFExgE%2BZpGGkslXNKg%3D&id4', '0%40U2got32sFUDDMtG9SNjzPN0YMhh%2B'], 
#                            'nk4': '',
#                            'tracknick': 'pdh521pdh',
#                            '_cc_': 'UIHiLt3xSw%3D%3D', 
#                            'tg': '0', 
#                            '_l_g_': 'Ug%3D%3D', 
#                            'sg': 'h64', 
#                            '_nk_': 'pdh521pdh', 
#                            'cookie1': 'VFR3DhwleDy1Dbn94FjX1qcUFMlgLN8S6Be6iV6f7Io%3D', 
#                            'enc': 'vFBEA3L7G7qPsHPgcRCz8xoQLYABs%2B2dyVjsfJTqV4smSOXwrA2iHhfGChJ8hYMN8TxWlKU%2BPcbyKDgy5y98BQ%3D%3D', 
#                            'JSESSIONID': 'A19FB86DDF13907A41E8B92F60F70AB5', 
#                            'hng': 'CN%7Czh-CN%7CCNY%7C156', 
#                            'uc1': ['cookie16', 'URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21', 'UIHiLt3xSifiVqTH8o%2F0Qw%3D%3D&cookie15', 'UIHiLt3xD8xYTw%3D%3D&existShop', 'false&pas', '0&cookie14', 'UoTbm8LS9X216A%3D%3D&tag', '8&lng', 'zh_CN'], 
#                            'cookie16':'',
#                            'mt': ['ci', '8_1'], 
#                            'ci': '',
#                            'l': 'dBQnSrsnqvCoUsP2BOCwhurza77O9IRfguPzaNbMi_5CE68lnD7OkUfTGFJ6cjXATk8BqdH2-se9xut7JjJcSlvX4AadZJk2B', 
#                            'isg': 'BCoqgiT6AxKvQ49-m_zzVtWXe5DMm671BdX-9rTj630F58uhnCvuBOjVc1LeFyaN'})
        browser.get('https://www.taobao.com/')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button'))
        )
        input.send_keys("美食")
        submit.click()
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total'))
        )
        get_products()
        return total.text
    
    except TimeoutError :
        return search()
        # 重新调用一次，递归

def next_page(page_number):
    print('正在翻页..')
    try:
        input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
            )
        submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'))
            )
        input.click()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))
        get_products()
    except TimeoutError:
        next_page(page_number)


def get_products():
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)

def save_to_mongo(result):
    print('正在保存到MongoDB..')
    try:
        if db[MONGO_TABLE].insert(result):
            print('存储到MongoDB成功！', result)
            return True
    except Exception:
        print('存储到MongoDB失败！', result)
                                                    
def main():
    try:
        total = search()
        total = int(re.compile('(\d+)').search(total).group(1))
        print(total)
        for i in range(2,total+1):
            next_page(i)
    except Exception:
        print('出错了')
    finally:
        browser.close()
        # 保证浏览器关闭
    
if __name__ == '__main__':
    main()
    
