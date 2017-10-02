# -*- coding: utf-8 -*-
from django.conf.urls import url
from album import views

urlpatterns = [
    #url(r'^$', views.first_view, name='first_view'),
    url(r'^$', views.base, name='base'),
    url(r'^category/$', views.category, name='category-list'),
    url(r'^category/(?P<category_id>\d+)/detail/$', views.category_detail, name='category-detail'),
    url(r'^photo/$', views.PhotoListView.as_view(), name='photo-list'),
    url(r'^photo/(\d+)/detail/$', views.photo_detail, name='photo-detail'),
    url(r'^photo/(?P<pk>\d+)/update/$', views.PhotoUpdate.as_view(), name='photo-update'),
    url(r'^photo/create/$', views.PhotoCreate.as_view(), name='photo-create'),
	url(r'^photo/(?P<pk>\d+)/delete/$', views.PhotoDelete.as_view(), name='photo-delete'),

]