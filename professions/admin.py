from django.contrib import admin
from django.contrib.admin import ModelAdmin

from professions.models import *


# Register your models here.

@admin.register(Profession)
class ProfessionAdmin(ModelAdmin):
    pass




