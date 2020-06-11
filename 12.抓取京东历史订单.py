# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import requests


browser = webdriver.Chrome()

def JDLogin():

    browser.get('https://passport.jd.com/new/login.aspx')

    QRcode = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[5]/div/div[2]/div[1]/img')
    QRurl = QRcode.get_attribute('src')
    
    return QRurl

def SaveQRimg(url):
    '''
    通过url链接将图片保存到本地jd.png
    '''
    r = requests.get(url)
    # 将获取到的图片二进制流写入本地文件
    with open('jd.png', 'wb') as f:
        # r.content 返回压缩格式的数据，一般图片之类的都是通过r.content获取
        f.write(r.content)
        
    return 0

def isElementExist(element):
    '''
    该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false   
    '''
    flag=True
    try:
        browser.find_element_by_css_selector(element)
        return flag
    
    except:
        flag=False
        return flag

def get_detail():
    '''
    获取订单信息
    '''
    # 等待我的订单链接加载好。。。
    input = WebDriverWait(browser,180,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#shortcut > div > ul.fr > li.shortcut_btn.fore2 > div > a')))
    print('succeed',input)
    
    # 选项
    browser.find_element_by_xpath('//*[@id="shortcut"]/div/ul[2]/li[3]/div/a').click()# 我的订单
    browser.switch_to.window(browser.window_handles[1])# 切换页面
    browser.find_element_by_css_selector('#orderState').click()# 全部订单下拉框
#    actions = ActionChains(browser)
#    actions.move_to_element(alldetail)
    
    browser.find_element_by_xpath('//*[@id="orderState"]/div[2]/ul/li[4]/a').click()# 已完成订单

    for page in range(1,10):
        browser.get('https://order.jd.com/center/list.action?s=1024&page='+str(page))
        if isElementExist('.empty-box'):
            print('没了')
            break
        else:
            herflis = browser.find_elements(By.CSS_SELECTOR, '.status a')# 获取订单链接列表
            print("长度为：", len(herflis))
            for herf in herflis:
                if herf.text=="订单详情" :
                    herf.click()# 进入单个订单详情页
                    browser.switch_to.window(browser.window_handles[2])# 切换页面
                    time.sleep(5)
                    print("进入成功")
                    detail()
                    browser.close()
                    browser.switch_to.window(browser.window_handles[1])
        #            break
                else:
                    continue
        
    return 0
        
def detail():
    '''
    在单个订单详情页获取信息
    '''
#    goods = browser.find_elements(By.CSS_SELECTOR, '#container > div.w > div > div.order-goods.m > div.mc > div.goods-list > table > tbody > tr.first-tr > ')
    time = browser.find_element_by_xpath('//*[@id="track_time_0"]')
    goods = browser.find_element(By.CSS_SELECTOR, '#container > div.w > div > div.order-goods.m > div.mc > div.goods-list > table > tbody > tr.first-tr')
    goodsname = goods.find_element(By.CSS_SELECTOR, 'div.p-name > a')
    goodsprice = goods.find_element(By.CSS_SELECTOR, '.f-price')
    goodsnum = goods.find_element(By.CSS_SELECTOR, 'td:nth-child(5)')
    goodssum = browser.find_element(By.CSS_SELECTOR, '#container > div.w > div > div.order-goods.m > div.mc > div.goods-total > ul > li.ftx-01 > span.txt.count')
    print("时间：",time.text)
    print("商品",goodsname.text)
    print("标价",goodsprice.text[1:])
    print("数量",goodsnum.text)
    print("实付价格",goodssum.text[1:])
    
    return 0

def Login(date, state, page):
    '''
    d=1 近三个月 2 今年 2019 2018...对应年份
    s=1024 已完成 4096 全部订单
    page=1 页码
    '''
    browser = webdriver.Chrome()
    browser.get('https://order.jd.com/center/list.action?d='+str(date)+'&s='+str(state)+'&page='+str(page))
    
    
    return 0

if __name__=='__main__':
#    Login(2019,1024,1)
    
    browser.get('https://passport.jd.com/new/login.aspx')
#    time.sleep(3)
    get_detail()
    
    time.sleep(3)
    
    browser.quit()
#    browser.switch_to_window(browser.window_handles[0])# 切换页面

