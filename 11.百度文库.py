# -*- coding: utf-8 -*-

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://wenku.baidu.com/view/52a30ce7ba4cf7ec4afe04a1b0717fd5360cb2e5.html')

# input_first = browser.find_element_by_css_selector('#reader-word-layer-s3-15')
# print(input_first)
# browser.find_element_by_xpath
time.sleep(10)

string = browser.find_element_by_xpath('//*[@id="pageNo-6"]/div/div/div/div[4]/div')

print(string.text)

with open('result.txt', 'a', encoding="utf-8") as f:
        f.write(string.text)
        f.close()
browser.close()


#pageNo-1 > div > div > div > div:nth-child(6) > div > p:nth-child(3)
