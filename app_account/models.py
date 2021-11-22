from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField

class UserManager(BaseUserManager):
    def create_user(self, parent, router,  password=None):

        user = self.model(
            parent=parent,
            router=router,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


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
    identification = models.CharField(max_length=30, null=True) #parents PK
    router = models.CharField(null=True, max_length=30)
    get_time = models.IntegerField(null=True)
    max_time = models.IntegerField(null=True)
    DATE_LIST = [
        (1, '월요일'),
        (2, '화요일'),
        (3, '수요일'),
        (4, '목요일'),
        (5, '금요일'),
        (6, '토요일'),
        (7, '일요일'),
    ]
    free_time = MultiSelectField(choices=DATE_LIST)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)

    self_objects = UserManager()


class Agreement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    term_agreement = models.BooleanField(null=True, )
    private_agreement = models.BooleanField(null=True, )
    geoLocation_agreement = models.BooleanField(null=True )
    provide_third_parties_agreement = models.BooleanField(null=True)
    marketing_agreement = models.BooleanField(null=True, blank=True)
    email_marketing_agreement = models.BooleanField(null=True, blank=True)
    sms_agreement = models.BooleanField(null=True, blank=True)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)