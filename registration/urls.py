from django.urls import path
from .views import *

urlpatterns = [
    path("signin/", signin_form, name="signin"),
    path("registration/", regist_form, name="registration_user"),
    path("signin/reg/", signin_reg, name="post_reg"),
    path("registration/reg/", reg_reg, name="signin_redirect"),
    path("api/authorization/userdb/", APIForAuthorisation.as_view(), name="authAPI"),
]
