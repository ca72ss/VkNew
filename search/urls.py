from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.login, name='main'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^forms$', views.forms, name='forms'),
    url(r'^create_message$', views.create_message, name='create_message'),
    url(r'^get_at$', views.get_at, name='get_at'),
    url(r'^get_name$', views.get_name, name='get_name'),
    url(r'^message$', views.message, name='message'),
    url(r'^intersection$', views.intersection, name='intersection'),
    url(r'^post_list$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^get_message$', views.get_message, name='get_message'),
    url(r'^visualisation$', views.visualisation, name='visualisation'),
    url(r'^info_forms$', views.info_forms, name='info_forms'),
    url(r'^info$', views.info, name='info'),

]
