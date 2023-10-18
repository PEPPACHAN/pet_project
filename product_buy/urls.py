from django.urls import path, include
from .views import *

urlpatterns = [
    path("product_list/", products_list, name="list"),
    path("product_detail/<int:product_id>/", product_detail, name="product_detail"),
    path("product_detaile/get_key/<int:product_id>/", get_key, name="get_key")
]
