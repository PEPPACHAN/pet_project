from django.urls import path, include
from .views import *

urlpatterns = [
    path("add_product/", add_products, name="add_products"),
    path("add_product/add_to_db/", add_to_db, name="test"),
]
