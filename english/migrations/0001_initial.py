# Generated by Django 3.2.9 on 2021-11-28 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('english', models.CharField(max_length=200, unique=True)),
                ('korean', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='uploadFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('file', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, max_length=20)),
                ('score', models.CharField(blank=True, max_length=20)),
                ('sentence1', models.CharField(blank=True, max_length=500)),
                ('answer1', models.CharField(blank=True, max_length=500)),
                ('voca1', models.CharField(blank=True, max_length=500)),
                ('sentence2', models.CharField(blank=True, max_length=500)),
                ('answer2', models.CharField(blank=True, max_length=500)),
                ('voca2', models.CharField(blank=True, max_length=500)),
                ('sentence3', models.CharField(blank=True, max_length=500)),
                ('answer3', models.CharField(blank=True, max_length=500)),
                ('voca3', models.CharField(blank=True, max_length=500)),
                ('sentence4', models.CharField(blank=True, max_length=500)),
                ('answer4', models.CharField(blank=True, max_length=500)),
                ('voca4', models.CharField(blank=True, max_length=500)),
                ('sentence5', models.CharField(blank=True, max_length=500)),
                ('answer5', models.CharField(blank=True, max_length=500)),
                ('voca5', models.CharField(blank=True, max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
