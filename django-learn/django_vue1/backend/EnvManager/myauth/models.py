from django.db import models


# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=50, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')

    class Meta:
        verbose_name = verbose_name_plural = '用户表'
        default_permissions = ('add_01', 'change_02', 'delete_03', 'view_04')
