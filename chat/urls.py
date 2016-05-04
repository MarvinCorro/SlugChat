from django.conf.urls import url

from . import views

app_name = 'chat'
urlpatterns = [
    url(r'^class_chat/', views.class_chat, name='class_chat'),
    url(r'^$', views.index, name='index'),
]