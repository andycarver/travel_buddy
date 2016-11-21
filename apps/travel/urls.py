from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_travel$', views.add_travel, name='add_travel'),
    url(r'^show/(?P<id>\d+)$', views.show, name='show'),
    url(r'^add_trip$', views.add_trip, name='add_trip'),
    url(r'^join_trip/(?P<id>\d+)$', views.join_trip, name='join_trip'),
]