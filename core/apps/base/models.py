from django.db import models

# Create your models here.
class InfoUser(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )