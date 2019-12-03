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
from bs4 import BeautifulSoup

html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
            <ul>
               <li>我校蝉联武书连2019中国民办大学综合实力排行榜第一</li>
               <li>我校连续三年位居广州日报应用大学排行榜民办本科高校第一名</li>
               <li>河南省教育厅专家组来我校调研基层教学组织建设情况</li>
            </ul>
          </div>      
         <li>图书馆举办 《党的十九届四中全会精神》专题党课学习会</li>
       
       <li>更多</li>
</div>'''

soup = BeautifulSoup(html, 'lxml')
print(soup.find_all('ul'))
print(type(soup.find_all('ul')[0]))# <class 'bs4.element.Tag'> 可以层层迭代
# 根据标签名查找文档,以列表形式返回结果


html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
            <ul>
               <li>我校蝉联武书连2019中国民办大学综合实力排行榜第一</li>
               <li>我校连续三年位居广州日报应用大学排行榜民办本科高校第一名</li>
               <li>河南省教育厅专家组来我校调研基层教学组织建设情况</li>
            </ul>
          </div>      
         <li>图书馆举办 《党的十九届四中全会精神》专题党课学习会</li>
       
       <li>更多</li>
</div>'''

soup = BeautifulSoup(html, 'lxml')
for ul in soup.find_all('ul'):
    print(ul.find_all('li'))
# 进一步迭代


html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
            <ul class="荣誉" id="list1">
               <li>我校蝉联武书连2019中国民办大学综合实力排行榜第一</li>
               <li name="ggg">我校连续三年位居广州日报应用大学排行榜民办本科高校第一名</li>
               <li>河南省教育厅专家组来我校调研基层教学组织建设情况</li>
            </ul>
            <ul class="新闻" id="list2">
                <li name="ggg">图书馆举办 《党的十九届四中全会精神》专题党课学习会</li>
                <li>更多</li>
            </ul>
    </div> 
</div>'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(attrs={'id':'con_com_1'}))
print(soup.find_all(attrs={'name':'ggg'}))
# 根据属性查找

print(soup.find_all(id='con_com_1'))
print(soup.find_all(class_='新闻'))
# 特殊的属性有自带的便捷方法可以用 （class_ 注意下划线）

html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
            <ul class="荣誉" id="list1">
               <li>我校蝉联武书连2019中国民办大学综合实力排行榜第一</li>
               <li name="ggg">我校连续三年位居广州日报应用大学排行榜民办本科高校第一名</li>
               <li>河南省教育厅专家组来我校调研基层教学组织建设情况</li>
            </ul>
            <ul class="新闻" id="list2">
                <li name="ggg">图书馆举办 《党的十九届四中全会精神》专题党课学习会</li>
                <li>更多</li>
                <li>更多</li>
            </ul>
    </div> 
</div>'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(text='更多'))
# 根据内容查找相对来说鸡肋一点，返回的就是你查找的内容

# =============================================================================
# find(name, attrs, recursive, text, **kwargs)
## find返回单个元素，find_all返回所有元素
from bs4 import BeautifulSoup
html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
            <ul class="荣誉" id="list1">
               <li>我校蝉联武书连2019中国民办大学综合实力排行榜第一</li>
               <li name="ggg">我校连续三年位居广州日报应用大学排行榜民办本科高校第一名</li>
               <li>河南省教育厅专家组来我校调研基层教学组织建设情况</li>
            </ul>
            <ul class="新闻" id="list2">
                <li name="ggg">图书馆举办 《党的十九届四中全会精神》专题党课学习会</li>
                <li>更多</li>
                <li>更多</li>
            </ul>
    </div> 
</div>'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find('ul'))
print(type(soup.find('ul')))
print(soup.find('page'))


# =============================================================================
# find_parents() find_parent()
# - find_parents()返回所有祖先结点
# - find_parent()返回父节点

# find_next_siblings() find_next_sibling()
# - find_next_siblings()返回后面所有兄弟结点
# - find_next_siblings()返回后面第一个兄弟结点

# find_previous_siblings() find_previous_sibling()
# - find_previous_siblings()返回前面所有兄弟结点
# - find_previous_siblings()返回前面第一个兄弟结点

# find_all_next() find_next()
# - find_all_next()返回节点后所有符合条件的结点
# - find_next()返回节点后第一个符合条件的结点

# find_all_previous() find_previous()
# - find_all_previous()返回节点后所有符合条件的结点
# - find_previous()返回节点后第一个符合条件的结点

# =============================================================================
# CSS选择器
## 通过select()直接传入css选择器即可完成选择
from bs4 import BeautifulSoup
html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
              Hi
          </div>
          <div>
            <ul class="荣誉" id="list1">
               <li name="txt">我校蝉联武书连2019中国民办大学综合实力排行榜第一</li>
               <li name="ggg">我校连续三年位居广州日报应用大学排行榜民办本科高校第一名</li>
               <li class="txt">河南省教育厅专家组来我校调研基层教学组织建设情况</li>
            </ul>
            <ul class="新闻" id="list2">
                <li name="ggg">图书馆举办 《党的十九届四中全会精神》专题党课学习会</li>
                <li>更多</li>
                <li>更多</li>
            </ul>
    </div> 
</div>'''
soup = BeautifulSoup(html, 'lxml')
print(soup.select('.Contentbox .hover'))
# 选择 “class=  ” 用“.”替代
print(soup.select('ul li'))
# 直接选择标签
print(soup.select('#list1 .txt'))
# 选择 “id=  ” 用“#”替代
print(type(soup.select('ul')[0]))


html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
              Hi
          </div>
          <div>
            <ul class="荣誉" id="list1">
               <li name="txt">我校蝉联武书连2019中国民办大学综合实力排行榜第一</li>
               <li name="ggg">我校连续三年位居广州日报应用大学排行榜民办本科高校第一名</li>
               <li class="txt">河南省教育厅专家组来我校调研基层教学组织建设情况</li>
            </ul>
            <ul class="新闻" id="list2">
                <li name="ggg">图书馆举办 《党的十九届四中全会精神》专题党课学习会</li>
                <li>更多</li>
            </ul>
    </div> 
</div>'''
soup = BeautifulSoup(html, 'lxml')
for ul in soup.select('ul'):
    print(ul.select('li'))
# 层层遍历打印出li，完全可以直接用soup.select('ul li')


# 获取属性
from bs4 import BeautifulSoup
html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
              Hi
          </div>
          <div>
            <ul class="荣誉" id="list1">
               <li name="txt">我校蝉联武书连2019中国民办大学综合实力排行榜第一</li>
               <li name="ggg">我校连续三年位居广州日报应用大学排行榜民办本科高校第一名</li>
               <li class="txt">河南省教育厅专家组来我校调研基层教学组织建设情况</li>
            </ul>
            <ul class="新闻" id="list2">
                <li name="ggg">图书馆举办 《党的十九届四中全会精神》专题党课学习会</li>
                <li>更多</li>
            </ul>
    </div> 
</div>'''
soup = BeautifulSoup(html, 'lxml')
for ul in soup.select('ul'):
    print(ul['id'])
#    print(ul.attrs['id'])
# 两种方法都可以获取属性


# 获取内容
from bs4 import BeautifulSoup
html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
              Hi
          </div>
          <div>
            <ul class="荣誉" id="list1">
               <li name="txt">我校蝉联武书连2019中国民办大学综合实力排行榜第一</li>
               <li name="ggg">我校连续三年位居广州日报应用大学排行榜民办本科高校第一名</li>
               <li class="txt">河南省教育厅专家组来我校调研基层教学组织建设情况</li>
            </ul>
            <ul class="新闻" id="list2">
                <li name="ggg">图书馆举办 《党的十九届四中全会精神》专题党课学习会</li>
                <li>更多</li>
            </ul>
    </div> 
</div>'''
soup = BeautifulSoup(html, 'lxml')
for li in soup.select('li'):
    print(li.get_text())
# 用get_text()获取内容

# =============================================================================
# 总结
#    - 推荐使用lxml解析库，代码非常混乱必要时使用html.parser解析库
#    - 标签选择筛选功能弱，但速度快
#    - 建议使用find(),find_all()查询匹配单个或多个结果
#    - 如果对CSS选择器熟悉建议使用select()
#    - 记住常用的获取属性和文本内容的方法


