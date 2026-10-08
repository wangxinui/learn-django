from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(null=True, blank=True) # 已经加上null=True


class Department(models.Model):
    name = models.CharField(max_length=32)

# class Role (models.Model):
#     name = models.CharField(max_length=16)