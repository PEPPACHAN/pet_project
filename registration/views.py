from django.contrib.auth import login
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore

from .models import *


# Create your views here.
users = Registered_Users.objects


@csrf_exempt
def regist_form(request):
    return render(request, "regist_form.html")


@csrf_exempt
def signin_form(request):
    return render(request, "signin_form.html")


@csrf_exempt
def signin_reg(request):
    if request.method == "POST":
        post_username = request.POST.get("username", "404")
        post_password = request.POST.get("password", "404")

        try:
            authorize = users.get(username=post_username)

        except:
            return HttpResponse("User doesn't exists")

        else:
            if check_password(post_password, authorize.password):

                # add users data
                request.session['user_id'] = 1
                request.session['username'] = post_username

                login(request, authorize)
                if request.user.username:
                    return HttpResponse(f"username == {request.user.username}<br>"
                                        f"password == {post_password}<br>"
                                        f"""<a href="{reverse('add_products')}">prod</a>""")
            else:
                return HttpResponse("Wrong password")


@csrf_exempt
def reg_reg(request):
    if request.method == "POST":
        post_username = request.POST.get("username", "404")
        post_password = request.POST.get("password", "404")
        post_image = request.POST.get("image", "404")

        try:
            users.get(username=post_username)

        except:
            reg_data = Registered_Users(username=post_username, password=make_password(post_password),
                                        user_image=post_image)
            reg_data.save()
            return HttpResponseRedirect(reverse("signin"))

        else:
            return HttpResponse("Already registered user or some error")
