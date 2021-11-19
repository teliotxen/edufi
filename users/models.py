from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#
# class User(AbstractUser):
#     nickname = models.CharField(max_length=15, null = True)
#     birthday = models.DateTimeField(null=True)
#     teacher = models.BooleanField(default=False)
#     paid_user = models.BooleanField(default=False, null=True)
#     share = models.BooleanField(default=False, null=True)
#     enrollment = models.DateTimeField(null=True)
#
# #useless
#     SCHOOL_TABLE = [
#         (1, "초등학교"),
#         (2, "중학교"),
#         (3, "고등학교")
#     ]
#     school = models.IntegerField(choices=SCHOOL_TABLE, default=None, null=True)
#     year = models.IntegerField(default=None, null=True)
#

