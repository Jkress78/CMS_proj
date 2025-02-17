from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserImg(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prof_img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.user.username