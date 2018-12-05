
from django.contrib import admin
from django.urls import path, re_path, include
from plusfriend import views

app_name='plusfriend'

urlpatterns = [
    re_path(r'^keyboard$', views.on_init),
    re_path(r'^friend$', views.on_added),
    re_path(r'^friend/(?P<user_key>[\w-]+)$', views.on_block),
    re_path(r'^chat_room/(?P<user_key>[\w-]+)$', views.on_leave),
    re_path(r'^message$', views.on_message),    
]
