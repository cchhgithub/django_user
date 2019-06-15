from django.db import models

# Create your models here.
class login_info(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class user_info(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    addr = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)