# sission 一般放在服务器上，常用来保存用户重要/敏感信息放在服务器上
# cookies 一般放在本地客户端Browser上，设置为防修改

# 分页器
from django.core.paginator import Paginator

# 假设Book是model里的一个模型表
books = Book.objects.all()

# 设置分页器
p = Paginator.(book, 20) # 参数中books是数据来源，20是单页数据量

print(p.count) # 总数量
print(p.num_pages) # 总页数
print(p.page_range) # 页码列表，从1开始

# 取第三页的内容，如果页码不存在，报InvalidPage异常
p.page(3)


# 基于类的视图
# - 可以针对http协议不同的方法创建不同的类
# - 可以使用Mixin等oop技术
# - Mixin
#     1. 把来自父类的行为或者属性组合到一起
#     2. 解决多重继承的问题

# - 可以实现列表视图 ListView
from django.views.generic import ListView

class BookListView(ListView):

	# 两个主要参数
	# 1. queryset: 数据来源
	queryset = Book.objects.all()
	# 2. template_name: 模板名称，模板是用来展示list数据的
	template_name = "books_list.html"

# urls.py 调用
path('book/', BookListView.as_view(), namespace=''),


