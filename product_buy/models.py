from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class ProductBuy(models.Model):
    username = models.ForeignKey("registration.Registered_Users", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_key = ArrayField(models.CharField(max_length=255))

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.product_name, self.product_key}"