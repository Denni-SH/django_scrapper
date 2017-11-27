
from django.conf.urls import url, include
from django.contrib import admin
from .views import index,success
urlpatterns = [
    url(r'^$', index),
    url(r'^success$', success),
]
