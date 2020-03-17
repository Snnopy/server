#coding=utf-8

from django.conf.urls import url
from Pmap import views

urlpatterns=[
    url(r'^register/$',views.index_view),
    url(r'^login/$',views.login_view),
    url(r'^reset/$',views.reset_view),
    url(r'^show/$',views.show_view),
    url(r'^$',views.login_view),  #默认为登录界面
]