from django.db import models
from registration.models import *


class product_sell(models.Model):
    username = models.ForeignKey(Registered_Users, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=150)
    product_description = models.TextField()
    sell_products = models.TextField()  # Create textfield and fill it by json data
    # Create condition check exist user or not

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username, self.product_name, self.product_description, self.sell_products
