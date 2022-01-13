from django.urls import re_path

from . import views

urlpatterns = [
          #超级用户
          
          #主页
          re_path(r'^$',views.index,name='index'),
          
          #show all blog
          re_path(r'^blogs/$',views.blogs,name='blogs'),
          
          #show blog
          re_path(r'^blogs/(?P<blog_id>\d+)/$',views.blog,name='blog'),
          
          #add new blog
          re_path(r'^new_blog/$',views.new_blog,name = 'new_blog'),
          re_path(r'^new_entry/(?P<blog_id>\d+)/$',views.new_entry,name='new_entry'),
          re_path(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'),
          ]
