from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tokensignin/', views.tokensignin, name='tokensignin'),
    url(r'^enroll/', views.enroll, name='enroll'),
    url(r'^addclass/', views.addclass, name='addclass'),
    url(r'^buildprofile/', views.buildprofile, name='buildprofile'),
    url(r'^$', views.profile, name='profilepage'),
]
