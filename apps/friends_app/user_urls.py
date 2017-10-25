from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^(?P<id>\d+)$", views.show),
    url(r"^error/$", views.error)
]	
