from django.conf.urls import url

from . import views

app_name = 'commenting'
urlpatterns = [
    # ex: /comments/
    url(r'^$', views.index, name='index'),
    
    # ex: /comments/5/
    # added the word 'specifics'
    url(r'^specifics/(?P<file_id>[0-9]+)/$', views.detail, name='detail'),
    
]