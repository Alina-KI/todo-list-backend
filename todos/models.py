from django.db import models


class Todo(models.Model):
    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    text = models.CharField(max_length=300, unique=True, verbose_name='Text')
    is_selected = models.BooleanField(default=False, verbose_name='IsSelected')
