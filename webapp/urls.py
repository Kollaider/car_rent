from django.urls import path

from webapp.views import index, about

app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
]
