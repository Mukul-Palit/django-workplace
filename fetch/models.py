from django.db import models

# Create your models here.
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=200)
    idd = models.BigAutoField(default=0, primary_key=True)
    privacy = models.CharField(max_length=100)
    admin = models.CharField(max_length=200)
    email = models.TextField()

    def __str__(self):
        return self.name, self.privacy, self.idd, self.admin, self.email


class Mem(models.Model):
    mname = models.CharField(max_length=200)
    midd = models.BigAutoField(default=0, primary_key=True)
    memail = models.TextField()
    madmin = models.BooleanField()
    mgroup = models.CharField(max_length=200)

    def __str__(self):
        return self.madmin, self.memail, self.mgroup, self.midd, self.mname



