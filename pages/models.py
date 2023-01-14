from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.db import models

from professions.models import Profession


# Create your models here.
class Page(models.Model):
    class Meta:
        db_table = "page"
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    page_name = models.CharField(max_length=50, unique=True, verbose_name="Название страницы")
    profession = models.ForeignKey(Profession, on_delete=models.RESTRICT, verbose_name="Профессия для страницы")

    def __str__(self):
        return f"{self.page_name}"


class Article(models.Model):
    class Meta:
        db_table = "article"
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    page = models.ForeignKey(Page, on_delete=models.RESTRICT, verbose_name="Страница статьи")
    profession = models.ForeignKey(Profession, on_delete=models.RESTRICT, verbose_name="Профессия статьи")
    title = models.CharField(max_length=150, blank=True)
    text = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return f"{self.page} / {self.profession.profession_name}: {self.title}"

# class Homepage(models.Model):
#     class Meta:
#         db_table = "homepage"
#         verbose_name = "Главная страница"
#         verbose_name_plural = "Главная страница"
#
#
#     profession = models.ForeignKey(Profession, on_delete=models.RESTRICT, verbose_name="Профессия главной страницы")
#     def save(self, *args, **kwargs):
#         if not self.pk and Homepage.objects.exists():
#             # if you'll not check for self.pk
#             # then error will also raised in update of exists model
#             raise ValidationError('There is can be only one Homepage instance')
#         return super(Homepage, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return f"{self._meta.verbose_name}: {self.profession}"
