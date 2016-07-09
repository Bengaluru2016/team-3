from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_page, name='index_page'),
    url(r'baseline/$', views.base_line, name='base_line'),
    url(r'health/$', views.health, name='base_line'),
]
