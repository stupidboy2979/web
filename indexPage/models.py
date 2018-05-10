from django.db import models

# Create your models here.


class Circuit(models.Model):
    trunk = models.IntegerField()
    port = models.CharField(max_length=20)
    sgNum = models.CharField(max_length=20)


class User(models.Model):
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    portal = models.CharField(max_length=20)
    das = models.IntegerField()
    dpc = models.CharField(max_length=20)
    creatDate = models.DateField(auto_now_add=False)
    circuits = models.ManyToManyField(Circuit)


