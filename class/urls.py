from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.class_chat, name='class_chat'),
]
