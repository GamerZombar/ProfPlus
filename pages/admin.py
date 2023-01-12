from django.contrib import admin
from django.contrib.admin import ModelAdmin

from pages.models import Homepage


# Register your models here.


@admin.register(Homepage)
class HomepageAdmin(ModelAdmin):
    pass