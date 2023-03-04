from django.urls import path

from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('post/<int:pk>', post, name='post'),
]
