from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<sector_id>[0-9]+)/$', views.move, name='move'),
    url(r'^new/$', views.new, name='new')
    
]
