# Generated by Django 3.2.9 on 2021-11-26 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_account', '0007_alter_router_max_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='free_time',
        ),
        migrations.RemoveField(
            model_name='user',
            name='max_time',
        ),
    ]