from django.db import models

# Create your models here.

from django.db import models


class Customer(models.Model):
    # 客户名称
    name = models.CharField(max_length=200)

    # 联系电话
    phone_number = models.CharField(max_length=200, null=True, blank=True)

    # 地址
    address = models.CharField(max_length=200)

    # 性别
    gender = models.CharField(max_length=10)
