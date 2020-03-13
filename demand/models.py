from django.db import models

# Create your models here.


class Demand(models.Model):
    STATUS_ITEMS = [
        (0, '未进行'),
        (1, '进行中'),
        (2, '已完成'),
    ]
    code = models.CharField(max_length=128, verbose_name="订单编号")
    requirement = models.CharField(max_length=128, verbose_name="订单需求")
    client = models.CharField(max_length=128, verbose_name="客户")
    number = models.CharField(max_length=128, verbose_name="订单数量")
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name="订单状态")
    time = models.CharField(max_length=128, verbose_name="交付日期")

    def __str__(self):
        return '<Demand:{}>'.format(self.code)

    class Meta:
        verbose_name = verbose_name_plural = "订单信息"
