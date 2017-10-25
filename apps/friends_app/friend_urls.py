from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^$", views.index),
    url(r"^add/(?P<id>\d+)$", views.add),
    url(r"^remove/(?P<id>\d+)$", views.remove),
    url(r"^error/$", views.error)
]	
