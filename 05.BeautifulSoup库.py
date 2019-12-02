# -*- coding: utf-8 -*-

# BeautifulSoup(markup,"")
# - 解析器
# Python标准库
# lxml HTML解析
# lxml XML解析
# html5lib
#
# - 使用方法
# BeautifulSoup(markup,"html.parser") Python的内置标准库、 执行速度适中、文档容错能力强
# BeautifulSoup(markup,"lxml") 速度快、文档容错能力强
# BeautifulSoup(markup,"xml") 速度快、唯一支持XML的解析器
# BeautifulSoup(markup,"html5lib") 最好的容错性、以浏览器的方式解析文档、生成HTML5格式的文档

from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<div id="wrapper" style="display: block;">
        
<div class="s_tab" id="s_tab">
<div class="s_tab_inner">
<b>网页</b>
<a href="//www.baidu.com/s?rtt=1&amp;bsst=1&amp;cl=2&amp;tn=news&amp;word=" wdfield="word" onmousedown="return c({'fm':'tab','tab':'news'})" sync="true">资讯</a>
<a href="http://tieba.baidu.com/f?kw=&amp;fr=wwwt" wdfield="kw" onmousedown="return c({'fm':'tab','tab':'tieba'})">贴吧</a>
<a href="http://zhidao.baidu.com/q?ct=17&amp;pn=0&amp;tn=ikaslist&amp;rn=10&amp;word=&amp;fr=wwwt" wdfield="word" onmousedown="return c({'fm':'tab','tab':'zhidao'})">知道</a>
</div>
</div>

<div class="qrcodeCon">
<div id="qrcode">
<div class="qrcode-item qrcode-item-1">
<div class="qrcode-img"></div>
<div class="qrcode-text">
<p class="title">下载百度APP</p>
<p class="sub-title">有事搜一搜&nbsp;&nbsp;没事看一看</p>
</div></div></div></div>
'''
soup =BeautifulSoup(html, 'lxml')
print("格式化：",soup.prettify())
print('标题：',soup.title.string)

# =============================================================================
# 标签选择器
## 选择元素
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<div id="wrapper" style="display: block;">
        
<div class="s_tab" id="s_tab">
<div class="s_tab_inner">
<b>网页</b>
<a href="//www.baidu.com/s?rtt=1&amp;bsst=1&amp;cl=2&amp;tn=news&amp;word=" wdfield="word" onmousedown="return c({'fm':'tab','tab':'news'})" sync="true">资讯</a>
<a href="http://tieba.baidu.com/f?kw=&amp;fr=wwwt" wdfield="kw" onmousedown="return c({'fm':'tab','tab':'tieba'})">贴吧</a>
<a href="http://zhidao.baidu.com/q?ct=17&amp;pn=0&amp;tn=ikaslist&amp;rn=10&amp;word=&amp;fr=wwwt" wdfield="word" onmousedown="return c({'fm':'tab','tab':'zhidao'})">知道</a>
</div>
</div>

<div class="qrcodeCon">
<div id="qrcode">
<div class="qrcode-item qrcode-item-1">
<div class="qrcode-img"></div>
<div class="qrcode-text">
<p class="title">下载百度APP</p>
<p class="sub-title">有事搜一搜&nbsp;&nbsp;没事看一看</p>
</div></div></div></div>
'''
soup =BeautifulSoup(html, 'lxml')
print(soup.title)
print(type(soup.title))
print(soup.head)
print(soup.p)
# 标签选择器只返回第一个匹配


## 获取名称
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<div id="wrapper" style="display: block;">
        
<div class="s_tab" id="s_tab">
<div class="s_tab_inner">
<b>网页</b>
<a href="//www.baidu.com/s?rtt=1&amp;bsst=1&amp;cl=2&amp;tn=news&amp;word=" wdfield="word" onmousedown="return c({'fm':'tab','tab':'news'})" sync="true">资讯</a>
<a href="http://tieba.baidu.com/f?kw=&amp;fr=wwwt" wdfield="kw" onmousedown="return c({'fm':'tab','tab':'tieba'})">贴吧</a>
<a href="http://zhidao.baidu.com/q?ct=17&amp;pn=0&amp;tn=ikaslist&amp;rn=10&amp;word=&amp;fr=wwwt" wdfield="word" onmousedown="return c({'fm':'tab','tab':'zhidao'})">知道</a>
</div>
</div>

<div class="qrcodeCon">
<div id="qrcode">
<div class="qrcode-item qrcode-item-1">
<div class="qrcode-img"></div>
<div class="qrcode-text">
<p class="title">下载百度APP</p>
<p class="sub-title">有事搜一搜&nbsp;&nbsp;没事看一看</p>
</div></div></div></div>
'''
soup =BeautifulSoup(html, 'lxml')
print(soup.title.name)
# 获取最外层标签名称


## 获取属性
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<div id="wrapper" style="display: block;">
        
<div class="s_tab" id="s_tab">
<div class="s_tab_inner">
<b>网页</b>
<a href="//www.baidu.com/s?rtt=1&amp;bsst=1&amp;cl=2&amp;tn=news&amp;word=" wdfield="word" onmousedown="return c({'fm':'tab','tab':'news'})" sync="true">资讯</a>
<a href="http://tieba.baidu.com/f?kw=&amp;fr=wwwt" wdfield="kw" onmousedown="return c({'fm':'tab','tab':'tieba'})">贴吧</a>
<a href="http://zhidao.baidu.com/q?ct=17&amp;pn=0&amp;tn=ikaslist&amp;rn=10&amp;word=&amp;fr=wwwt" wdfield="word" onmousedown="return c({'fm':'tab','tab':'zhidao'})">知道</a>
</div>
</div>

<div class="qrcodeCon">
<div id="qrcode">
<div class="qrcode-item qrcode-item-1">
<div class="qrcode-img"></div>
<div class="qrcode-text">
<p class="title">下载百度APP</p>
<p class="sub-title">有事搜一搜&nbsp;&nbsp;没事看一看</p>
</div></div></div></div>
'''
soup =BeautifulSoup(html, 'lxml')
print(soup.p.attrs['class'])
print(soup.p['class'])
# 获取标签本身属性值


## 获取内容
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<div id="wrapper" style="display: block;">
        
<div class="s_tab" id="s_tab">
<div class="s_tab_inner">
<b>网页</b>
<a href="//www.baidu.com/s?rtt=1&amp;bsst=1&amp;cl=2&amp;tn=news&amp;word=" wdfield="word" onmousedown="return c({'fm':'tab','tab':'news'})" sync="true">资讯</a>
<a href="http://tieba.baidu.com/f?kw=&amp;fr=wwwt" wdfield="kw" onmousedown="return c({'fm':'tab','tab':'tieba'})">贴吧</a>
<a href="http://zhidao.baidu.com/q?ct=17&amp;pn=0&amp;tn=ikaslist&amp;rn=10&amp;word=&amp;fr=wwwt" wdfield="word" onmousedown="return c({'fm':'tab','tab':'zhidao'})">知道</a>
</div>
</div>

<div class="qrcodeCon">
<div id="qrcode">
<div class="qrcode-item qrcode-item-1">
<div class="qrcode-img"></div>
<div class="qrcode-text">
<p class="title">下载百度APP</p>
<p class="sub-title">有事搜一搜&nbsp;&nbsp;没事看一看</p>
</div></div></div></div>
'''
soup =BeautifulSoup(html, 'lxml')
print(soup.p.string)
# 获取标签内的内容


## 嵌套选择
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<div id="wrapper" style="display: block;">
        
<div class="s_tab" id="s_tab">
<div class="s_tab_inner">
<b>网页</b>
<a href="//www.baidu.com/s?rtt=1&amp;bsst=1&amp;cl=2&amp;tn=news&amp;word=" wdfield="word" onmousedown="return c({'fm':'tab','tab':'news'})" sync="true">资讯</a>
<a href="http://tieba.baidu.com/f?kw=&amp;fr=wwwt" wdfield="kw" onmousedown="return c({'fm':'tab','tab':'tieba'})">贴吧</a>
<a href="http://zhidao.baidu.com/q?ct=17&amp;pn=0&amp;tn=ikaslist&amp;rn=10&amp;word=&amp;fr=wwwt" wdfield="word" onmousedown="return c({'fm':'tab','tab':'zhidao'})">知道</a>
</div>
</div>

<div class="qrcodeCon">
<div id="qrcode">
<div class="qrcode-item qrcode-item-1">
<div class="qrcode-img"></div>
<div class="qrcode-text">
<p class="title">下载百度APP</p>
<p class="sub-title">有事搜一搜&nbsp;&nbsp;没事看一看</p>
</div></div></div></div>
'''
soup =BeautifulSoup(html, 'lxml')
print(soup.head.title.string)
# head -> title -> 内容 （层层剥离，迭代）


## 子节点和孙子结点
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<div id="wrapper" style="display: block;">
        
<div class="s_tab" id="s_tab">
<div class="s_tab_inner">
<b>网页
<a href="//www.baidu.com/s?rtt=1&amp;bsst=1&amp;cl=2&amp;tn=news&amp;word=" wdfield="word" onmousedown="return c({'fm':'tab','tab':'news'})" sync="true">资讯</a>
<a href="http://tieba.baidu.com/f?kw=&amp;fr=wwwt" wdfield="kw" onmousedown="return c({'fm':'tab','tab':'tieba'})">贴吧</a>
<a href="http://zhidao.baidu.com/q?ct=17&amp;pn=0&amp;tn=ikaslist&amp;rn=10&amp;word=&amp;fr=wwwt" wdfield="word" onmousedown="return c({'fm':'tab','tab':'zhidao'})">知道</a>
</b></div>
</div>
'''
soup =BeautifulSoup(html, 'lxml')
print(soup.b.contents)
print(type(soup.b.contents))
# 以列表的形式返回孩子节点的内容(不进一步剥离孙子结点)


html = '''
<html><head><title>The Dormouse's story</title></head>
<div id="wrapper" style="display: block;">
        
<p class="s_tab_inner">
<b>网页
<a href="//www.baidu.com/s?rtt=1&amp;bsst=1&amp;cl=2&amp;tn=news&amp;word=" wdfield="word" onmousedown="return c({'fm':'tab','tab':'news'})" sync="true">资讯</a>
<a href="http://tieba.baidu.com/f?kw=&amp;fr=wwwt" wdfield="kw" onmousedown="return c({'fm':'tab','tab':'tieba'})">贴吧</a>
<a href="http://zhidao.baidu.com/q?ct=17&amp;pn=0&amp;tn=ikaslist&amp;rn=10&amp;word=&amp;fr=wwwt" wdfield="word" onmousedown="return c({'fm':'tab','tab':'zhidao'})">知道</a>
</b>
</p>
</div>
'''
soup =BeautifulSoup(html, 'lxml')
print(soup.b.children)
print(type(soup.b.children))
for l,child in enumerate(soup.b.children):
    print(l,child)
# 以迭代器的形式返回孩子节点的内容(不进一步剥离孙子结点)


html = '''
<html><head><title>The Dormouse's story</title></head>
<div id="wrapper" style="display: block;">
        
<p class="s_tab_inner">
<b>网页
<a href="//www.baidu.com/s?rtt=1&amp;bsst=1&amp;cl=2&amp;tn=news&amp;word=" wdfield="word" onmousedown="return c({'fm':'tab','tab':'news'})" sync="true">资讯</a>
<a href="http://tieba.baidu.com/f?kw=&amp;fr=wwwt" wdfield="kw" onmousedown="return c({'fm':'tab','tab':'tieba'})">贴吧</a>
<a href="http://zhidao.baidu.com/q?ct=17&amp;pn=0&amp;tn=ikaslist&amp;rn=10&amp;word=&amp;fr=wwwt" wdfield="word" onmousedown="return c({'fm':'tab','tab':'zhidao'})">知道</a>
</b>
</p>
</div>
'''
soup =BeautifulSoup(html, 'lxml')
print(soup.b.descendants)
print(type(soup.b.descendants))
for l,child in enumerate(soup.b.descendants):
    print(l,child)
# 以迭代器的形式返回孩子节点和孙子的内容，进一步剥离孙子结点


## 父节点和祖先结点
html = '''
<html><head><title>The Dormouse's story</title></head>
<div id="wrapper" style="display: block;">
        
<p class="s_tab_inner">
<b>网页
<a href="//www.baidu.com/s?rtt=1&amp;bsst=1&amp;cl=2&amp;tn=news&amp;word=" wdfield="word" onmousedown="return c({'fm':'tab','tab':'news'})" sync="true">资讯</a>
<a href="http://tieba.baidu.com/f?kw=&amp;fr=wwwt" wdfield="kw" onmousedown="return c({'fm':'tab','tab':'tieba'})">贴吧</a>
<a href="http://zhidao.baidu.com/q?ct=17&amp;pn=0&amp;tn=ikaslist&amp;rn=10&amp;word=&amp;fr=wwwt" wdfield="word" onmousedown="return c({'fm':'tab','tab':'zhidao'})">知道</a>
</b>
</p>
</div>
'''
soup =BeautifulSoup(html, 'lxml')
print(soup.a.parent)
# 查找第一个a的父节点，打印





# =============================================================================
html = '''
<html><head><title>The Dormouse's story</title></head>
<div id="wrapper" style="display: block;">
        
<p class="s_tab_inner">
<b>网页
<a href="//www.baidu.com/s?rtt=1&amp;bsst=1&amp;cl=2&amp;tn=news&amp;word=" wdfield="word" onmousedown="return c({'fm':'tab','tab':'news'})" sync="true">资讯</a>
<a href="http://tieba.baidu.com/f?kw=&amp;fr=wwwt" wdfield="kw" onmousedown="return c({'fm':'tab','tab':'tieba'})">贴吧</a>
<a href="http://zhidao.baidu.com/q?ct=17&amp;pn=0&amp;tn=ikaslist&amp;rn=10&amp;word=&amp;fr=wwwt" wdfield="word" onmousedown="return c({'fm':'tab','tab':'zhidao'})">知道</a>
</b>
</p>
</div>
'''
soup =BeautifulSoup(html, 'lxml')

print(list(enumerate(soup.a.parents)))
print(soup.a.parents)
# 找到a的所有祖先结点

# =============================================================================
# 兄弟结点
html = '''
<html><head><title>The Dormouse's story</title></head>
<div id="wrapper" style="display: block;">
        
<p class="s_tab_inner">
<b>网页
<a href="//www.baidu.com/s?rtt=1&amp;bsst=1&amp;cl=2&amp;tn=news&amp;word=" wdfield="word" onmousedown="return c({'fm':'tab','tab':'news'})" sync="true">资讯</a>
<a href="http://tieba.baidu.com/f?kw=&amp;fr=wwwt" wdfield="kw" onmousedown="return c({'fm':'tab','tab':'tieba'})">贴吧</a>
<a href="http://zhidao.baidu.com/q?ct=17&amp;pn=0&amp;tn=ikaslist&amp;rn=10&amp;word=&amp;fr=wwwt" wdfield="word" onmousedown="return c({'fm':'tab','tab':'zhidao'})">知道</a>
</b>
</p>
</div>
'''
soup =BeautifulSoup(html, 'lxml')
print(list(enumerate(soup.a.next_siblings)))
# 后面的兄弟结点
print(list(enumerate(soup.a.previous_siblings)))
# 前面的兄弟结点

# =============================================================================
# 标准选择器
# - find_all(name,attrs,recursive,text,**kwargs)
# - 可根据标签名，属性，内容查找文档




# =============================================================================
# 


# =============================================================================
# 