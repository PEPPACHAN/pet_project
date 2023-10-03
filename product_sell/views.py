from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt

from registration.models import *
from .models import *


@csrf_exempt
def add_products(request):
    return render(request, "add_product.html")


@csrf_exempt
def add_to_db(request):  # product_name description key price
    if request.session.get("username") is not None:
        username = request.session.get('username')
        user = get_object_or_404(Registered_Users, username=username)
        post_product_name = request.POST.get("product_name", "404")
        post_description = request.POST.get("description", "404")
        post_key = request.POST.get("key", "404")
        post_price = request.POST.get("price", "error")

        if post_key[-1] == ",":
            post_key[-1].replace(",", "")
        elif post_key[1] == ",":
            post_key[1].replace(",", "")
        key_set = set(post_key.replace(" ", "").split(","))
        if "" in key_set:
            key_set.remove("")

        try:
            ProductSell.objects.get(
                username=user,
                product_name=post_product_name
            )
        except:
            product = ProductSell(
                username=user,
                product_name=post_product_name,
                product_description=post_description,
                product_price=post_price,
                product_keys=list(key_set)
            )
            product.save()
            data = ProductSell.objects.get(username=user, product_name=post_product_name)
            return HttpResponse(f"{data.product_keys}<br>")

        else:
            data = ProductSell.objects.get(username=user, product_name=post_product_name)
            update_key = set(data.product_keys)
            update_key.update(key_set)
            update_key.discard("")

            data.product_keys = update_key
            return HttpResponse("Data was filled<br>"
                                f"{data.product_keys}<br>")

    else:
        return HttpResponseRedirect(reverse("signin"))

# def buy_a_key(request):
