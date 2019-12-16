# -*- coding: utf-8 -*-

"""
@author: cht
@time: 2019/8/10 15:23
"""

import csv
from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.action_chains import ActionChains

class TaoBaoPersonOrder(object):
    def start_taobao(self):
        # 1.创建chrom浏览器对象
        driver = webdriver.Chrome()
        # 2.打开淘宝登录网址
        driver.get(
            'https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.201864-2.d1.5af911d9oPmC7G&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F')
        # 3.点击登录
        # driver.find_element_by_name('登录').click()
#        driver.find_element_by_xpath('//*[@id="J_QRCodeLogin"]/div[5]/a[1]').click()
        # 选择微博登录
#        driver.find_element_by_xpath('//*[@id="J_OtherLogin"]/a[1]').click()
        # 选择二维码登录
        #driver.find_element_by_xpath('//*[@id="J_Static2Quick"]').click()
        sleep(10)
        # 4.输入账号和密码
#        driver.find_element_by_name("username").clear()
#        driver.find_element_by_name("username").send_keys("18339474940")
#        driver.find_element_by_name('password').clear()
#        driver.find_element_by_name("password").send_keys("pdh5216919")
#        driver.find_element_by_xpath('//*[@class="btn_tip"]/a/span').click()

        # 5.悬浮在我的淘宝 #定位 添加条件 按钮，经观需要鼠标悬停
        sleep(2)

        move_on_to_add_condition = driver.find_element_by_xpath('//*[@id="J_SiteNavMytaobao"]/div[1]/a/span')
        ActionChains(driver).move_to_element(move_on_to_add_condition).perform()
        #6.点击已买到的宝贝
        sleep(2)
        driver.find_element_by_link_text('已买到的宝贝').click()

        # 休眠2秒
        sleep(2)
        # 1.打开文件 encoding=utf-8 指定文件的字符编码
        file_handle = open('C:\\Users\\Administrator\\Desktop\\laguodata\\personorder.csv', 'w', encoding='utf-8')

        for y in range(1, 3):
            print('正在获取第%s页数据，请稍后......' % y)
            # for 循环执行5次
            for x in range(1, 10, 2):
                # 休眠1秒
                sleep(1)
                # 把x转换小数
                j = x / 10
                # 拼接让浏览器滚动的js代码
                # %f float类型数据占位符
                js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight *%f ' % j
                # 执行让浏览器滚动的js代码
                driver.execute_script(js)

            # 查找当前页所有的商品信息,返回的是一个列表（elements查找多个）
            # 电脑，鼠标、键盘.........class_name填写 info-cont
            # 其他的产品........class_name填写 J_MouserOnverReq
            shops = driver.find_elements_by_class_name('js-order-container')
            # print(len(shops))
            # 如果没有找到数据，换另一种方式去找
            if len(shops) == 0:
                print('出错了')
                # shops = driver.find_elements_by_class_name('info-cont')

            # for循环遍历列表，取出每一个商品的信息
            file = open('C:\\Users\\Administrator\\Desktop\\laguodata\\personorder.csv', 'a+', newline='',
                        encoding='utf-8')  # 打开文件
            content = csv.writer(file, dialect='excel')  # 设定文件写入模式
            for shop in shops:
                # 输出查看商品信息
                line_list = shop.text.split('\n')
                del line_list[5:]
                if line_list[3].find('￥')== 0 and line_list[4].find('￥') == 0:

                    del line_list[3]

                content.writerow(line_list)

            # 找到下一页，点击
            # 找到li标签下一页
            try:
                url_input = driver.find_element_by_xpath('//*[@id="tp-bought-root"]/div[19]/div[2]/ul/div/div/input')
                url = driver.find_element_by_xpath('//*[@id="tp-bought-root"]/div[19]/div[2]/ul/div/div/span[3]')
                url_input.clear()
                y += 1
                url_input.send_keys(y)
                time.sleep(3)
                print('准备跳转')
                #该span只能定位，不能只点击,采用点击加悬浮的方式
                webdriver.ActionChains(driver).move_to_element(url).click(url).perform()
                print('----------------------')
                sleep(5)
            except Exception as e:
                print(e)
                print('跳转第%s页出问题'%y)
                break
        # 3.关闭文件
        # 退出浏览器
        driver.quit()


# 如果是从当前文件直接运行的，执行以下代码
if __name__ == '__main__':

    tb = TaoBaoPersonOrder()
    tb.start_taobao()

