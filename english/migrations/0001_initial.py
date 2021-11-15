# Generated by Django 3.2.9 on 2021-11-15 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=20)),
                ('word1', models.CharField(max_length=20)),
                ('word1_switch', models.CharField(max_length=20)),
                ('word1_korean', models.CharField(max_length=20)),
                ('word2', models.CharField(blank=True, max_length=20)),
                ('word2_switch', models.CharField(blank=True, max_length=20)),
                ('word2_korean', models.CharField(blank=True, max_length=20)),
                ('word3', models.CharField(blank=True, max_length=20)),
                ('word3_switch', models.CharField(blank=True, max_length=20)),
                ('word3_korean', models.CharField(blank=True, max_length=20)),
                ('english', models.CharField(max_length=200)),
                ('korean', models.CharField(max_length=200)),
            ],
        ),
    ]
