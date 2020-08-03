from django.db import models


# Create your models here.

class Environment(models.Model):
    STATUS_OFFLINE = 0
    STATUS_ONLINE = 1
    STATUS_ITEM = (
        (STATUS_OFFLINE, '离线'),
        (STATUS_ONLINE, '在线')
    )
    name = models.CharField(max_length=50, verbose_name='环境名称')
    url = models.CharField(max_length=50, verbose_name='访问地址')
    status = models.IntegerField(default=0, choices=STATUS_ITEM, verbose_name='在线状态')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    remark = models.CharField(max_length=200,blank=True, verbose_name='备注')

    class Meta:
        db_table = 'environment'
