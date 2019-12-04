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




 