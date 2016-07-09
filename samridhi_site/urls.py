from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_page, name='index_page'),
    url(r'health/$', views.health, name='health'),
    url(r'survey/$', views.survey, name='survey'),
    url(r'attend/$', views.attendance, name='attendance'),
    url(r'login/$', views.login, name='login'),
    url(r'sendsms/$', views.sendsms, name='sendsms'),
]
