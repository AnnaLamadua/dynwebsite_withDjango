# -*- coding:utf8 -*-

from django.conf.urls import url

from simplesite.views import IndexDetailView, PageDetailView

app_name = 'simplesite'
urlpatterns = [
    url(r'^$', IndexDetailView.as_view(), kwargs={'slug': 'home'}, name='home_page'),
    url(r'^(?P<slug>[-\w]+)/$', PageDetailView.as_view(), name='page_detail'),
]
