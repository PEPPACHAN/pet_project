from django.urls import path, include
from .views import *

urlpatterns = [
    path("add_product/", add_products, name="add_products"),
    path("add_product/add_to_db/", add_to_db, name="test"),
    path("product_list/", products_list, name="list"),
    path("product_detail/<int:product_id>/", product_detail, name="product_detail"),
    path("product_detaile/get_key/<int:product_id>/", get_key, name="get_key")
]
