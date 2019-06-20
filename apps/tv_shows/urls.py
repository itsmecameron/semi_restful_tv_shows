from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^shows$', views.index),
    url(r'^shows/new$', views.add_show),
    url(r'^process$', views.process),
    url(r'^update$', views.update),
    url(r'^shows/(?P<val>\d+)$', views.show),
    url(r'^shows/edit/(?P<val>\d+)$', views.edit),
    url(r'^delete/(?P<val>\d+)', views.destroy),
]