from django.contrib import admin
from django.contrib.admin import ModelAdmin

from pages.models import Page, Article  # , Homepage


# Register your models here.

@admin.register(Page)
class PageAdmin(ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    pass
