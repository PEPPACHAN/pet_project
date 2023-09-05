from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
users = Registered_Users.objects


def regist_form(request):
    context = {}

    return render(request, "regist_form.html")


def signin_form(request):
    context = {"username": users, "password": users}

    return render(request, "signin_form.html", context=context)


def signin_reg(request):
    if request.method == "POST":
        post_username = request.POST.get("username", "404")
        post_password = request.POST.get("password", "404")

        if users.get(username=post_username, password=post_password):
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

    reg_data = db(username=f"post_username", password=f"post_password", user_image=post_image)
    return reg_data.save()
