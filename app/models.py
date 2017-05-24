from __future__ import unicode_literals

from django.db import models

class user(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    mobile=models.CharField(max_length=11,unique=True)
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    duty=models.CharField(max_length=50)

class need(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    need_id=models.IntegerField(null=True)
    need_name=models.CharField(max_length=100)
    need_status=models.CharField(max_length=20)
    finish_test=models.CharField(max_length=10)
    need_tester=models.CharField(max_length=20)
    need_day=models.CharField(max_length=30)
    need_url=models.CharField(max_length=150)
    beizhu=models.CharField(max_length=150)


