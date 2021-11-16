from django.contrib import admin
from .models import Quiz, uploadFileModel
# Register your models here.

class QuizAdmin(admin.ModelAdmin):
    list_display = (
        'english',
        'korean',
        'level',
        'word1',
        'word2',
        'word3',
    )


admin.site.register(Quiz,QuizAdmin)
admin.site.register(uploadFileModel)
