from django.db import models
from django.contrib.postgres.fields import ArrayField


class ProductSell(models.Model):
    username = models.ForeignKey("registration.Registered_Users", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=150)
    product_description = models.TextField()
    product_price = models.IntegerField(default=0)
    product_keys = ArrayField(models.CharField(max_length=100))

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.product_name, self.product_price}"


class ProductBuy(models.Model):
    username = models.ForeignKey("registration.Registered_Users", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_key = ArrayField(models.CharField(max_length=255))
    buy_date = ArrayField(models.DateTimeField(auto_now=True, auto_now_add=False))

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.product_name}"
