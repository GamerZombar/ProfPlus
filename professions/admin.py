from django.contrib import admin
from django.contrib.admin import ModelAdmin

from professions.models import Profession


# Register your models here.

@admin.register(Profession)
class TeacherAdmin(ModelAdmin):
    pass
