from django.db import models

# Create your models here.


class Profession(models.Model):
    class Meta:
        db_table = "profession"
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"

    profession_name = models.CharField(max_length=150)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.profession_name}"
