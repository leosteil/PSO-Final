from django.conf.urls import url, include
from django.contrib import admin
from auth_google import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'} ,name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^home/$', views.home,name='home'),
    url(r'^$', views.index, name='index'),
]