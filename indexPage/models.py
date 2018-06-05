from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Circuit(models.Model):
    trunk = models.IntegerField()
    port = models.CharField(max_length=20)
    sgNum = models.CharField(max_length=20)
    location = models.CharField(max_length=20)


class MgcfCode(models.Model):
    updated_at = models.DateField(auto_now_add=True)
    updated_by = models.CharField(max_length=20)
    code = models.CharField(max_length=1000)
    remarks = models.CharField(max_length=100, null=True)


class MgwCode(models.Model):
    updated_at = models.DateField(auto_now_add=True)
    updated_by = models.CharField(max_length=20)
    code = models.CharField(max_length=1000)
    remarks = models.CharField(max_length=100, null=True)


class SssCode(models.Model):
    updated_at = models.DateField(auto_now_add=True)
    updated_by = models.CharField(max_length=20)
    code = models.CharField(max_length=1000)
    remarks = models.CharField(max_length=100, null=True)


class Number(models.Model):
    num = models.CharField(max_length=20, unique=True)
    physical_num = models.CharField(max_length=20, unique=True, null=True)


class Company(models.Model):
    name = models.CharField(max_length=20, unique=True)
    numbers = models.ForeignKey(Number, related_name='company', on_delete=models.CASCADE)
    location = models.CharField(max_length=20)
    portal = models.CharField(max_length=10)
    das = models.IntegerField(unique=True)
    dpc = models.CharField(max_length=11, unique=True)
    remarks = models.CharField(max_length=100, null=True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.CharField(max_length=20)
    circuits = models.ManyToManyField(Circuit)
    mgcf_code = models.ForeignKey(MgcfCode, related_name='company', on_delete=models.CASCADE)
    mgw_code = models.ForeignKey(MgwCode, related_name='company', on_delete=models.CASCADE)
    sss_code = models.ForeignKey(SssCode, null=True, related_name='company', on_delete=models.CASCADE)


