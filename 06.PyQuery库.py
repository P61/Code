# -*- coding: utf-8 -*-

from pyquery import PyQuery as pq
html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
              Hi
          </div>
          <div>
            <ul class="荣誉" id="list1">
               <li name="txt">我校蝉联武书连2019中国第一</li>
               <li name="ggg">我校连续三年位居广州第一名</li>
               <li class="txt">河南省教育厅专家组来情况</li>
            </ul>
    </div> 
</div>'''
doc = pq(html)
print(doc('li'))

# =============================================================================
# URL 初始化
from pyquery import PyQuery as pq
doc = pq(url='http://www.baidu.com')
print(doc('head'))


# =============================================================================
# 文件初始化
from pyquery import PyQuery as pq
doc = pq(filename='demo.html')
print(doc('li'))

# =============================================================================
# 基本CSS选择器
from pyquery import PyQuery as pq
html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
              Hi
          </div>
          <div>
            <ul class="hor" id="list1">
               <li name="txt">我校蝉联武书连2019中国第一</li>
               <li name="ggg">我校连续三年位居广州第一名</li>
               <li class="txt">河南省教育厅专家组来情况</li>
            </ul>
    </div> 
</div>'''
doc = pq(html)
print(doc('.Contentbox #list1 li'))
print(doc('.Contentbox li'))
# 后面的标签和前面的有层级关系，但不是一定是它的子标签

# =============================================================================
# 查找元素
## 子元素
from pyquery import PyQuery as pq
html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
              Hi
          </div>
          <div>
            <ul class="hor" id="list1">
               <li name="txt">我校蝉联武书连2019中国第一</li>
               <li name="ggg">我校连续三年位居广州第一名</li>
               <li class="txt t"><a class="t">aaa</a>河南省教育厅专家组来情况</li>
               <li class="item1 t">河南省教育厅专</li>
            </ul>
    </div> 
</div>'''
doc = pq(html)
items = doc('.hor')
print(type(items))
print(items)
lis = items.find('li')# 找到items里(不一定是直接子标签)的所有li标签，还能递进查找里面的子元素
print(type(lis))
print(lis)


doc = pq(html)
items = doc('.hor')
lis = items.children() # 查找直接子元素
print(type(lis))
print(lis)


doc = pq(html)
items = doc('.hor')
lis = items.children('.t') # 查找直接子元素的...
print(lis)

# =============================================================================
# 父元素
from pyquery import PyQuery as pq
html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
              Hi
          </div>
          <div id="con_com_2" class="click">
            <ul class="hor" id="list1">
               <li name="txt">我校蝉联武书连2019中国第一</li>
               <li name="ggg">我校连续三年位居广州第一名</li>
               <li class="txt t"><a class="t">aaa</a>河南省教育厅专家组来情况</li>
               <li class="item1 t">河南省教育厅专</li>
            </ul>
    </div> 
</div>'''
doc = pq(html)
items = doc(".hor")
content = items.parent()# 查找直接父节点
print(type(content))
print(content)


doc = pq(html)
items = doc(".hor")
content = items.parents()# 查找所有祖先结点，并分别返回
print(type(content))
print(content)


doc = pq(html)
items = doc(".hor")
content = items.parents('.hover')# 在祖先结点内筛选
print(content)


# =============================================================================
# 兄弟元素
from pyquery import PyQuery as pq
html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
              Hi
          </div>
          <div id="con_com_2" class="click">
            <ul class="hor" id="list1">
               <li name="txt">我校蝉联武书连2019中国第一</li>
               <li name="ggg">我校连续三年位居广州第一名</li>
               <li class="txt t"><a class="t">aaa</a>河南省教育厅专家组来情况</li>
               <li class="item1">河南省教育厅专</li>
            </ul>
    </div> 
</div>'''
doc = pq(html)
li = doc('#list1 .txt.t')# .txt.t 中间不加空格表示是一个整体
print(li.siblings())
# 选择所有的兄弟结点

doc = pq(html)
li = doc('#list1 .txt.t')# .txt.t 中间不加空格表示是一个整体
print(li.siblings('.item1'))
# 在兄弟结点里再次筛选

# =============================================================================
# 遍历
## 单个元素
from pyquery import PyQuery as pq
html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
              Hi
          </div>
          <div id="con_com_2" class="click">
            <ul class="hor" id="list1">
               <li name="txt">我校蝉联武书连2019中国第一</li>
               <li name="ggg">我校连续三年位居广州第一名</li>
               <li class="txt t"><a class="t">aaa</a>河南省教育厅专家组来情况</li>
               <li class="item1">河南省教育厅专</li>
            </ul>
    </div> 
</div>'''
doc = pq(html)
li = doc('.item1')
print(li)

# 多个元素
lis = doc('li').items()
print(type(lis))# <class 'generator'>
for li in lis:
    print(li)


# =============================================================================
# 获取信息
## 获取属性
from pyquery import PyQuery as pq
html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
              Hi
          </div>
          <div id="con_com_2" class="click">
            <ul class="hor" id="list1">
               <li name="txt">我校蝉联武书连2019中国第一</li>
               <li name="ggg">我校连续三年位居广州第一名</li>
               <li class="txt"><a class="t" href="www.ssasasas.com" >aaa</a>河南省教育厅专家组来情况</li>
               <li class="item1">河南省教育厅专</li>
            </ul>
    </div> 
</div>'''
doc = pq(html)
a = doc('.txt a')
print(a)
print(a.attr('href'))
print(a.attr.href)
# 使用attr来获取属性

# 获取文本
html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
              Hi
          </div>
          <div id="con_com_2" class="click">
            <ul class="hor" id="list1">
               <li name="txt">我校蝉联武书连2019中国第一</li>
               <li name="ggg">我校连续三年位居广州第一名</li>
               <li class="txt"><a class="t" href="www.ssasasas.com" >河南省教育厅专家组来情况</a></li>
               <li class="item1">河南省教育厅专</li>
            </ul>
    </div> 
</div>'''
doc = pq(html)
a = doc('.txt')
print(a)
print(a.text())
# 使用text来获取属性


# 获取HTML
html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
              Hi
          </div>
          <div id="con_com_2" class="click">
            <ul class="hor" id="list1">
               <li name="txt">我校蝉联武书连2019中国第一</li>
               <li name="ggg">我校连续三年位居广州第一名</li>
               <li class="txt"><a class="t" href="www.ssasasas.com" >河南省教育厅专家组来情况</a></li>
               <li class="item1">河南省教育厅专</li>
            </ul>
    </div> 
</div>'''
doc = pq(html)
li = doc('.txt')
print(li)
print(li.html())
# 获取a里面一层的html代码

# =============================================================================
# DOM操作(节点操作)
from pyquery import PyQuery as pq
html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
              Hi
          </div>
          <div id="con_com_2" class="click">
            <ul class="hor" id="list1">
               <li name="txt">我校蝉联武书连2019中国第一</li>
               <li name="ggg">我校连续三年位居广州第一名</li>
               <li class="txt"><a class="t" href="www.ssasasas.com" >河南省教育厅专家组来情况</a></li>
               <li class="item1">河南省教育厅专</li>
            </ul>
    </div> 
</div>'''
doc = pq(html)
li = doc('.txt')
print(li)
li.removeClass('txt')# 删除class的txt属性
print(li)
li.addClass('txt')# 添加class的txt属性
print(li)


# attr、css
html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
              Hi
          </div>
          <div id="con_com_2" class="click">
            <ul class="hor" id="list1">
               <li name="txt">我校蝉联武书连2019中国第一</li>
               <li name="ggg">我校连续三年位居广州第一名</li>
               <li class="txt" style="font-size: 10px"><a class="t" href="www.ssasasas.com" >河南省教育厅专家组来情况</a></li>
               <li class="item1">河南省教育厅专</li>
            </ul>
    </div> 
</div>'''
doc = pq(html)
li = doc('.txt')
print(li)
li.attr('name', 'link')# 不存在该属性添加，存在修改
print(li)
li.css('font-size', '14px')# 不存在该属性添加，存在修改
print(li)



# remove
html = '''
<div class="Contentbox" valign="top">
    Hello
          <p id="con_com_1" class="hover">
              Hi
          </p>
          <p id="con_com_1" class="hover">
              Hi1
          </p>
</div>'''
doc = pq(html)
con = doc('.Contentbox')
print(con.text())
con.find('p').remove()# 删除所有p标签的所有内容
print(con.text())

# 其他DOM方法
# - http://pyquery.readthedocs.io/en/latest/api.html

# =============================================================================
# 伪类选择器
from pyquery import PyQuery as pq
html = '''
<div class="Contentbox" valign="top"> 
          <div id="con_com_1" class="hover">
              Hi
          </div>
          <div id="con_com_2" class="click">
            <ul class="hor" id="list1">
               <li name="txt">我校蝉联武书连2019中国第一</li>
               <li name="ggg">我校连续三年位居广州第一名</li>
               <li class="txt" style="font-size: 10px"><a class="t" href="www.ssasasas.com" >河南省教育厅专家组来情况</a></li>
               <li class="item1">河南省教育厅专</li>
            </ul>
    </div> 
</div>'''
doc = pq(html)
li = doc('li:first-child')# 第一个li标签
print(li)
li = doc('li:last-child')# 最后一个li标签
print(li)
li = doc('li:nth-child(2)')# 第二个li标签
print(li)
li = doc('li:gt(1)')# 序号大于第一个的li标签，234
print(li)           # eq相等 ne、neq不相等，gt大于，lt小于 gte、ge大于等于 lte、le 小于等于
li = doc('li:nth-child(2n)')# 序号为偶数的标签
print(li)
li = doc('li:contains(我校)')# 查找包含某个文本的li标签
print(li)

# 更多的CSS选择器可以查看 http://www.w3school.com.cn/css/index.asp

 