from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user  = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "People"