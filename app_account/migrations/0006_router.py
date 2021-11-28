# Generated by Django 3.2.9 on 2021-11-26 02:08

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app_account', '0005_auto_20211123_0935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('router_id', models.CharField(max_length=20, unique=True)),
                ('max_time', models.IntegerField(max_length=24)),
                ('free_time', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '월요일'), (2, '화요일'), (3, '수요일'), (4, '목요일'), (5, '금요일'), (6, '토요일'), (7, '일요일')], max_length=13)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
