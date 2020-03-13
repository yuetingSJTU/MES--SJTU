# Generated by Django 3.0.3 on 2020-02-23 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128, verbose_name='订单编号')),
                ('requirement', models.CharField(max_length=128, verbose_name='订单需求')),
                ('client', models.CharField(max_length=128, verbose_name='客户')),
                ('number', models.CharField(max_length=128, verbose_name='订单数量')),
                ('status', models.IntegerField(choices=[(0, '未进行'), (1, '进行中'), (2, '已完成')], default=0, verbose_name='订单状态')),
                ('time', models.DateTimeField(verbose_name='交付日期')),
            ],
            options={
                'verbose_name': '学员信息',
                'verbose_name_plural': '学员信息',
            },
        ),
    ]
