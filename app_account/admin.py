from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Agreement

admin.site.register(Agreement)
admin.site.register(User, UserAdmin )
UserAdmin.fieldsets += (("Custom fields", {"fields": ("parent","phone","name","birthday","school","gender","identification","get_time","max_time","free_time", 'router')}),)
