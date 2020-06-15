import re

# 邮箱
# ^([a-z0-9\+_\-]+)(\.[a-z0-9\+_\-]+)*@([a-z0-9\-]+\.)+[a-z]{2,6}$
# 手机号
# ^1[3|4|5|6|7|8][0-9]\d{8}$


# .	 匹配除换行符以外的任意字符
# \w	匹配字母或数字或下划线[a-z|A-Z|0-9|_]
# \W 匹配非 字母或数字或下划线
# \s	匹配任何不可见字符，包括空格、制表符、换页符等等。等价于[ \f\n\r\t\v]。
# \S	匹配任何可见字符。等价于[^ \f\n\r\t\v]。
# \d	匹配数字
# \D	匹配非数字
# \b	匹配单词的开始或结束
# \B	匹配不是单词开头或结束的位置
# ^	匹配字符串的开始
# $	匹配字符串的结束
# [^x]	匹配除了x以外的任意字符
# [^aeiou]	匹配除了aeiou这几个字母以外的任意字符

# *	重复零次或更多次
# +	重复一次或更多次(贪婪)
# ?	重复零次或一次(非贪婪)
# {n}	重复n次
# {n,} 重复n次或更多次
# {n,m}	重复n到m次

# re.match
# - 尝试从字符串的起始位置匹配一个模式。
# - 如果不是起始位置匹配成功的话，match()就返回none
a = 'phyt3hyy78ohn45'
rsm = re.match(r'y', a)
print(rsm)

# re.search
# - 扫描整个字符串并返回第一个成功的匹配
rss = re.search(r'y', a)
print(rss,rss.group())

# re.findall
# - 在字符串中找到正则表达式匹配到的所有子串，并返回一个列表
# - 如果没有匹配到就返回空列表
rsf = re.findall(r'y', a)
print(rsf)

# re.compile
# - 用于编译正则表达式，生成一个正则表达式对象(re.Pattern)
res = re.compile(r'\d+')
result = re.findall(res, a)
print(result)

# re.sub()替换正则匹配的部分
b = re.sub(res, 'KKK', a)
print(b)

# re.split()
# - 根据匹配的分割字符串，返回分割后的列表，匹配中的内容删除
b = re.split(res, a)
print(b)

# import requests

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# url = 'https://book.douban.com/'
# html = requests.get(url, headers=headers)
# # print(html.text)

# res = re.compile(r'src="(.+?jpg)"')
# reg = re.findall(res, html.text)
# print(reg)


str = "copyright 2003"
ret = re.search(r'[0-9]+',str)
print(ret)