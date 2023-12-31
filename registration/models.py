from django.db import models


# Create your models here.
class Registered_Users(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    user_image = models.ImageField(default="media/default.png", upload_to="media/user_media")
    last_login = models.DateTimeField(auto_now=False, auto_now_add=True)  # reserved for login function

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username
