from django.urls import path
from .views import *

urlpatterns = [
    path("signin/", signin_form, name="signin"),
    path("registration/", regist_form, name="registration_user"),
    path("signin/reg/", signin_reg, name="post_reg"),
    path("registration/reg/", signin_form, name="signin_after_reegistration"),
    path("registration/reg/reg/", signin_reg, name="signin_after_reegistration_after_registration"),
]
