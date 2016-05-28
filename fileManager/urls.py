from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'upload', views.upload_file, name='upload'),
    url(r'download', views.download_file, name='download'),
]
