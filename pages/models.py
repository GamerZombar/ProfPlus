from django.core.exceptions import ValidationError
from django.db import models

from professions.models import Profession


# Create your models here.

class Homepage(models.Model):
    class Meta:
        db_table = "homepage"
        verbose_name = "Главная страница"
        verbose_name_plural = "Главная страница"

    profession = models.ForeignKey(Profession, on_delete=models.RESTRICT, verbose_name="Профессия главной страницы")

    def save(self, *args, **kwargs):
        if not self.pk and Homepage.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('There is can be only one Homepage instance')
        return super(Homepage, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self._meta.verbose_name}: {self.profession}"
