from django.db import models

from ..module.module import Module


class Lesson(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    module = models.ForeignKey(Module, related_name="lessons", on_delete=models.CASCADE)
    start_date = models.DateField()

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

        db_table = "lesson"
        ordering = ["name"]

    def __str__(self):
        return f"O curso {self.name} pertence ao modulo {self.module}"
