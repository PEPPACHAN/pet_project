from django.contrib import admin
from .models import *


class ProductSellAdmin(admin.ModelAdmin):
    list_display = ("username", "product_name", "product_price")
    fields = ["username", "product_name", "product_description","product_keys", "product_price"]

    def custom_array_field_display(self, obj):
        return ", ".join(map(str, obj.product_keys))


ProductSellAdmin.custom_array_field_display.short_description = "Array Field"


admin.site.register(ProductSell, ProductSellAdmin)
