
from django.conf.urls import url, include
from django.contrib import admin
from .views import index,success, ProductsPage, PricesPage

urlpatterns = [
    url(r'^$', index),
    url(r'^success$', success),
    url(r'^products$', ProductsPage.as_view()),
    url(r'^prices$', PricesPage.as_view()),
]
