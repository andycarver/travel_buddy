from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index, name='index'),
    url(r"^create$", views.create, name='create'),
    url(r"^add_trip$", views.add_trip, name='add_trip'),
    url(r"^show/(?P<id>\d+)/$", views.show, name='show'),
    url(r"^join$", views.join, name='join'),
]