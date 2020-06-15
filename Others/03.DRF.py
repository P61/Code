# 创建项目django ，名为DRF
# 管理员用户python manage.py createsuperuser
# 新建一个app（case01），创建Model类，迁移数据库python manage.py makemigrations/migrate

# - 在DRF/case01/下新建serializers.py
from django.contrib.auth.models import User, Group 
# User, Group是Django自带的数据库结构
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
# 在这个例子中我们用到了超链接关系，使用 HyperlinkedModelSerializer。
# 你还可以使用主键和各种其他关系，但超链接是好的RESTful设计。


# - DRF/case01/Views
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from DRF.case01.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# - 配置DRF/DRF/urls
from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

# 使用自动URL路由连接我们的API。
# 另外，我们还包括支持浏览器浏览API的登录URL。
urlpatterns = [
	path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # 我们将包括用于支持浏览器浏览的API的默认登录和注销视图。这是可选的，但如果您的API需要身份验证，并且你想要使用支持浏览器浏览的API，那么它们很有用。
]


# - 配置settings,
#     - 在INSTALLED_APPS中将 rest_framework 和新建的app（case01）注册
INSTALLED_APPS = (
    ...
    'rest_framework',
    'case01',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10# 分页
}
# 我们也想设置一些全局设置。我们想打开分页，我们希望我们的API只能由管理员使用。


# 现在你就可访问 http://127.0.0.1:8000/api/ 以及 
# 		http://127.0.0.1:8000/api/users


# 序列化/反序列化
















