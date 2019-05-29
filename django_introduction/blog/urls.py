from django.urls import path, include

import blog.views


urlpatterns = [
    path("hello_world", blog.views.hello_world), #如果地址含有hello_world，就转发到视图里
    path("content",blog.views.article_content),
]
