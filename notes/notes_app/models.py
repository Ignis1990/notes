from django.db import models


class Note(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Имя заметки',
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок заметки',
    )
    description = models.TextField(
        verbose_name='Описание заметки',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

