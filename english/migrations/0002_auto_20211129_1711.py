# Generated by Django 3.2.9 on 2021-11-29 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='korean1',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='korean2',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='korean3',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='korean4',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='korean5',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
