from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import *
from product_sell.models import *
from registration.models import *


# Create your views here.
def products_list(request):
    data = ProductSell.objects.all()
    context = {"products": data}

    return render(request, "products_list.html", context=context)


def product_detail(request, product_id):
    data = get_object_or_404(ProductSell, pk=product_id)
    return render(request, "product_detail.html", context={"product": data})


def get_key(request, product_id):
    user = get_object_or_404(Registered_Users, username=request.session.get("username"))
    product = ProductSell.objects.get(pk=product_id)
    if request.session.get("username") is not None:
        try:
            ProductBuy.objects.get(username=user, product_name=product.product_name)
        except ObjectDoesNotExist:
            if product.product_keys is not None:
                buyer = ProductBuy(
                    username=user,
                    product_name=product.product_name,
                    product_key=list(product.product_keys.pop())
                )
                product.save()
                buyer.save()
                return HttpResponse(f"{buyer}")
        else:
                print(product.product_keys)
                basket = ProductBuy.objects.get(username=user, product_name=product.product_name)
                update_key = basket.product_key
                try:
                    update_key.append(product.product_keys.pop())
                except IndexError:
                    product.delete()
                    return HttpResponseRedirect(reverse("list"))
                else:
                    print(update_key)
                    basket.product_key = update_key

                basket.save()
                product.save()
                return HttpResponse(f"{basket}")

