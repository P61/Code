# -*- coding: utf-8 -*-

# https://tool.oschina.net/regex/  在线正则匹配测试，一些常用简单的正则

# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，macth()就返回none
# re.match(pattern,string,flags=0)

## 最常规的匹配
import re

content = 'Hello 234 1234 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
# \s 断点
print(result)
print(result.group())
print(result.span())

# =============================================================================
# 范匹配
import re

content = 'Hello 234 1234 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$',content)
print(result)
print(result.group())
print(result.span())

# 匹配目标
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld.*Demo$',content)
print(result)
print(result.group(1))
print(result.span())
# 正则表达式里括号括起来的会按照顺序放进 group(1),group(2),...

# =============================================================================
# 贪婪匹配
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$',content)
# ^He.* 贪婪的匹配了 Hello 123456 只留下了一个数字7给\d
print(result)
print(result.group(1))


# 非贪婪匹配
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$',content)
# ^He.*? 非贪婪留下了最多的数字给\d
print(result)
print(result.group(1))

# 个人体会：贪婪是尽可能的给前面的匹配多
#           非贪婪是尽可能的给后面的匹配多

# =============================================================================
# 匹配模式
import re

content = '''Hello 1234567 World_This 
is a Regex Demo
'''

result = re.match('^He.*?(\d+).*Demo$',content)
print(result)
result = re.match('^He.*?(\d+).*Demo$',content,re.S)
print(result.group(1))
# . 不能匹配换行符，加上re.S参数后可以

# 转义字符
import re

content = 'price is $5.00'
result = re.match('price is $5.00',content)
print(result)
# \ 代表转义字符
result = re.match('price is \$5\.00',content)
print(result.group())

# =============================================================================
# 小结：尽量使用范匹配'.*'、使用括号获得匹配目标'()'、尽量使用非贪婪模式'?'、有换行符就用re.S
# =============================================================================

# re.search
# - 扫描整个字符串并返回第一个成功的匹配。

import re
# match
content = 'Extra stings Hello 123456 World_This is a Regex Demo Extra stings'
result = re.match('Hello.*?(\d+).*?Demo',content)
print(result)
# search
result = re.search('Hello.*?(\d+).*?Demo',content)
print(result)
print(result.group(1))

# 为了方便能用search就不用match
# =============================================================================

# 匹配练习
import re
html = '''
<div id="container navigation">
	<h2 class="title">经典老歌</h2>
    <p class='introduction'>
        经典老歌列表
    </p>
		<ul id="list" class="list-group">
			<li data-view="2">一路上有你</li>
			<li data-view="7">
    			<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
			</li>
			<li data-view="4" class="active">
			<a href="/3.mp3" singer="齐秦">往事随风</a>
			</li>
			<li data-view="6"><a href="/4.mp3" singer="Beyond">光辉岁月</a></li>
			<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
			<li data-view="5">
    			<a harf="/6.mp3" singer="邓丽君">但愿人长久</a>
			</li>
		</ul>
</div>'''

result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result.group(1),result.group(2))

result = re.search('<li.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result.group(1),result.group(2))

result = re.search('<li.*?singer="(.*?)">(.*?)</a>',html)
print(result.group(1),result.group(2))


# =============================================================================
# re.findall 
# - 找到所有符合结果的子串，用列表形式返回
import re
html = '''
<div id="container navigation">
	<h2 class="title">经典老歌</h2>
    <p class='introduction'>
        经典老歌列表
    </p>
		<ul id="list" class="list-group">
			<li data-view="2">一路上有你</li>
			<li data-view="7">
    			<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
			</li>
			<li data-view="4" class="active">
			<a href="/3.mp3" singer="齐秦">往事随风</a>
			</li>
			<li data-view="6"><a href="/4.mp3" singer="Beyond">光辉岁月</a></li>
			<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
			<li data-view="5">
    			<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
			</li>
		</ul>
</div>'''



results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
print(results)
for k in results:
#    print(k)
    print(k[1])

# =============================================================================
# re.sub 方法替换
import re

html = re.sub('<a.*?>|</a>','',html)
print(html)
results = re.findall('<li.*?>(.*?)</li>',html,re.S)
print(results)
for k in results:
    print(k.strip())



