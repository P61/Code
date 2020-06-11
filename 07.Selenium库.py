# -*- coding: utf-8 -*-


# 帮组文档 https://selenium-python-zh.readthedocs.io/en/latest/index.html

# 基本使用
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
#    print(browser.page_source)
finally:
#    pass
    browser.close()


# =============================================================================
# 声明浏览器对象
from selenium import webdriver

browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser = webdriver.Edge()
browser = webdriver.PhantomJS()
browser = webdriver.Safari()
    
# =============================================================================
# 访问页面
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
print(browser.page_source)
browser.close()

# =============================================================================
# 查找元素
## 查找单个元素
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
browser.close()
# 多种查找方式
# browser.find_element_by_class_name
# browser.find_element_by_css_selector
# browser.find_element_by_id
# browser.find_element_by_link_text
# browser.find_element_by_name
# browser.find_element_by_partial_link_text
# browser.find_element_by_tag_name
# browser.find_element_by_xpath


# 通用方法
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element(By.ID, 'q')
print(input_first)
browser.close()



## 多个元素
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis)
browser.close()
# 列表形式返回

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
print(lis)
print(lis[2])
browser.close()

# browser.find_elements_by_class_name
# browser.find_elements_by_css_selector
# browser.find_elements_by_id
# browser.find_elements_by_link_text
# browser.find_elements_by_name
# browser.find_elements_by_partial_link_text
# browser.find_elements_by_tag_name
# browser.find_elements_by_xpath



## 元素交互操作
## - 对获取的元素调用交互方法

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('手机')
time.sleep(1)
input.clear()
input.send_keys('电脑')
button = browser.find_element_by_class_name('btn-search')
button.click()

# 更多操作：http://selenium-python.readthedocs.io/api.html#model-selenium.webdriver.remote.webelement

# =============================================================================
# 交互动作
## 将动作附加到动作链中串行执行
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
# 拖拽动作

# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains

# =============================================================================
# 执行JavaScript
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
# 通过调用JS执行下拉进度条操作

# =============================================================================
# 获取元素信息
## 获取属性
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
logo = browser.find_element_by_class_name('Icon--logo')
print(logo)
print(logo.get_attribute('width'))
print(logo.get_attribute('height'))
# 获取logo的长宽

## 获取文本值
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('AppHeader-TabsLink')
print(input.text)
# 获取文本

## 获取ID、位置、标签名、大小
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('AppHeader-TabsLink')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)


# Frame切换
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
print(source)
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException as e:
    print('NO LOGO')
    print(e)
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)
# 切换到父Frame查找logo

# =============================================================================
# 等待
## 隐式等待(实用性较差)
## - 等待一定时间，时间到了没有找到就报错 
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('AppHeader-TabsLink1')
print(input)

## 显示等待(常用)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
wait = WebDriverWait(browser,10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'btn-search')))
print(input, button)

#更多等待的条件：https://selenium-python.readthedocs.io/waits.html
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
# =============================================================================
# 前进后退
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.get('https://www.python.org')
browser.get('https://www.taobao.com')
browser.back()
time.sleep(1)
browser.forward()
browser.close()


# =============================================================================
# Cookies
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name':'name', 'domain':'www.zhihu.com', 'value':'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())

# =============================================================================
# 选项卡管理
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://www.python.org')
# 通过执行js打开一个新的选项卡，选项卡之间的切换

# =============================================================================
# 异常处理
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.find_element_by_id('hello')


from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print("Time Out")
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print("No Element")
finally:
    browser.close()

# 更多异常捕获 https://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions
