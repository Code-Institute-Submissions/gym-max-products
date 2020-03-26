from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import product_list, product_detail

urlpatterns = [
    url('^$', product_list, name="product_list"),
    url('^$', product_detail, name="product_detail"),
]