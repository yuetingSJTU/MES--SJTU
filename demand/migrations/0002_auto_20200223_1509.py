# Generated by Django 3.0.3 on 2020-02-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demand',
            options={'verbose_name': '订单信息', 'verbose_name_plural': '订单信息'},
        ),
        migrations.AlterField(
            model_name='demand',
            name='time',
            field=models.CharField(max_length=128, verbose_name='交付日期'),
        ),
    ]