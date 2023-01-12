from django.db import models

# Create your models here.

# class Page(models.Model):
#     class Meta:
#         db_table = "page"
#         verbose_name = "Главная страница"
#         verbose_name_plural = "Главные страницы"





from ckeditor_uploader.fields import RichTextUploadingField

class Profession(models.Model):
    class Meta:
        db_table = "profession"
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"

    profession_name = models.CharField(max_length=150)
    title_img = models.ImageField(upload_to="media/static/profession/img", null=True, blank=True)
    short_description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.profession_name}"


class Blog(models.Model):
    class Meta:
        db_table = "blog"
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    profession = models.ForeignKey(Profession, on_delete=models.RESTRICT, verbose_name="Профессия блога")
    title = models.CharField(max_length=150, blank=True)
    text = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return f"{self.profession.profession_name}: {self.title}"
