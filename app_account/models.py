from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField

# class UserManager(BaseUserManager):
#     def create_user(self, parent, router,  password=None):
#
#         user = self.model(
#             parent=parent,
#             router=router,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user


class User(AbstractUser):
    parent = models.BooleanField(default=False)
    phone = models.CharField(null=True, max_length=12)
    name = models.CharField(max_length=15, null = True)
    birthday = models.DateField(null=True)
    school = models.CharField(max_length=15, null = True)
    gender_table = [
        (1, "남"),
        (2, "여"),
        (3, "응답하지 않음")
    ]
    gender = models.IntegerField(choices=gender_table, default=None, null=True)
    grade_table = [
        (1, "초등3"),
        (2, "초등4"),
        (3, "초등5"),
        (4, "초등6"),
        (5, "중등1"),
        (6, "중등2"),
        (7, "중등3"),
    ]
    grade = models.IntegerField(choices=grade_table, default=None, null=True)
    identification = models.CharField(max_length=30, null=True) #parents PK
    router = models.CharField(null=True, max_length=30)
    get_time = models.IntegerField(default=0)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)

    # self_objects = UserManager()


class Router(models.Model):
    router_id = models.CharField(max_length=20, unique=True)
    minute_list = [
        (5, '5분'),
        (10, '10분'),
        (15, '15분'),
        (20, '20분'),
        (25, '25분'),
        (30, '30분'),

    ]
    get_time = models.IntegerField(choices=minute_list ,null=True)
    hour_list = [
        (30, '30분'),
        (60, '1시간'),
        (90, '1시간 30분'),
        (120, '2시간'),
        (150, '2시간 30분'),
        (180, '3시간'),
        (210, '3시간 30분'),
        (240, '4시간'),
    ]
    max_time = models.IntegerField(choices=hour_list)
    DATE_LIST = [
        (1, '월요일'),
        (2, '화요일'),
        (3, '수요일'),
        (4, '목요일'),
        (5, '금요일'),
        (6, '토요일'),
        (7, '일요일'),
    ]
    free_time = MultiSelectField(choices=DATE_LIST, blank=True)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.router_id


class Agreement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    term_agreement = models.BooleanField(default=False,)
    private_agreement = models.BooleanField(default=False )
    geoLocation_agreement = models.BooleanField(default=False )
    provide_third_parties_agreement = models.BooleanField(default=False)
    marketing_agreement = models.BooleanField(default=False, null=True)
    email_marketing_agreement = models.BooleanField(default=False, null=True)
    sms_agreement = models.BooleanField(null=True, default=False)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)