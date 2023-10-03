from django.contrib import admin
from .models import Registered_Users


# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("username", "password", "last_login")
    fields = ["user_image", "username", "password"]


admin.site.register(Registered_Users, RegistrationAdmin)
