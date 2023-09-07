from django.contrib.auth import login
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
users = Registered_Users.objects


def regist_form(request):
    context = {"username": users, "password": users, "image": users}

    post_username = request.POST.get("username", "404")
    post_password = request.POST.get("password", "404")
    post_image = request.POST.get("image", "media/default.png")

    registrate = Registered_Users(username=post_username, password=make_password(post_password), user_image=post_image)
    registrate.save()

    # login(post_username, post_password)

    return render(request, "regist_form.html", context=context)


def signin_form(request):
    context = {"username": users, "password": users}

    return render(request, "signin_form.html", context=context)


def signin_reg(request):
    if request.method == "POST":
        post_username = request.POST.get("username", "404")
        post_password = request.POST.get("password", "404")

        autorize = users.get(username=post_username)
        if check_password(post_password, autorize.password):
            login(request, autorize)
            return HttpResponse(f"username == {users.get(username=post_username).username}<br>"
                                f"password == {post_password}<br>")

        else:
            return HttpResponse("Some ERROR. Data in db is:<br>"
                                f"{users.get(username=post_username, password=post_password)}<br>"
                                "POST data is:<br>"
                                f"{post_username}<br>"
                                f"{post_password}")


def reg_reg(request):
    post_username = request.POST.get("username", "404")
    post_password = request.POST.get("password", "404")
    post_image = request.POST.get("image", "404")

    reg_data = Registered_Users(username=post_username, password=make_password(post_password), user_image=post_image)
    reg_data.save()

    return redirect("http://127.0.0.1:8000/signin/")


def redirect_to_signin(request):
    return redirect("http://127.0.0.1:8000/signin/")