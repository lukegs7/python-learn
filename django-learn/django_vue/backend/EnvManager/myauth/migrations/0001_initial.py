# Generated by Django 2.2.10 on 2020-06-05 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'default_permissions': ('add_01', 'change_02', 'delete_03', 'view_04'),
            },
        ),
    ]
