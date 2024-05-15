"""solidersys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Adminlogin.views import *
from Students.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),

    ##添加vue版本###
    path('add', Add_info.as_view(), name="Add_info"),
    ##添加 微信小程序 版本###
    path('adds', Add.as_view(), name="Add_info"),
    ##搜索查看######
    path('query', Query_info.as_view(), name="Query_info"),
    ##删除，按照学号删除##
    path('delete', Delet_info.as_view(), name="Delet_info"),
    ##登录方法，
    # path('login', Login.as_view(), name="login"),
    path('login', GetUserView.as_view(), name="user"),
]
