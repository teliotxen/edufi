# Generated by Django 3.2.9 on 2021-12-08 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_account', '0006_alter_user_get_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='grade',
            field=models.IntegerField(choices=[(1, '초등3'), (2, '초등4'), (3, '초등5'), (4, '초등6'), (5, '중등1'), (6, '중등2'), (7, '중등3')], default=None, null=True),
        ),
    ]
