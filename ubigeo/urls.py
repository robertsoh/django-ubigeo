# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^provincias/$', views.ProvinciaView.as_view(), name='provincias'),
    url(r'^distritos/$', views.DistritoView.as_view(), name='distritos'),
]
