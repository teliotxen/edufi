from django.db import models

# Create your models here.


class Quiz(models.Model):
    level = models.CharField(max_length=20, blank=False)
    word1 = models.CharField(max_length=20, blank=False)
    word1_switch = models.CharField(max_length=20, blank=False)
    word1_korean = models.CharField(max_length=20, blank=False)

    word2 = models.CharField(max_length=20, blank=True)
    word2_switch = models.CharField(max_length=20, blank=True)
    word2_korean = models.CharField(max_length=20, blank=True)

    word3 = models.CharField(max_length=20, blank=True)
    word3_switch = models.CharField(max_length=20, blank=True)
    word3_korean = models.CharField(max_length=20, blank=True)

    english = models.CharField(max_length=200, blank=False, unique=True)
    korean = models.CharField(max_length=200, blank=False)


class uploadFileModel(models.Model):
    title = models.TextField(default='')
    file = models.FileField(null=True)