from django.db import models


class Module(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = "module"
        verbose_name_plural = "modules"

        db_table = "module"
        ordering = ["name"]

    def __str__(self):
        return self.name
