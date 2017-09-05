
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<name_id>[0-9]+)$', views.get_name, name='get_name'),
]
