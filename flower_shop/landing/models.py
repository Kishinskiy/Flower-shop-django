from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=100, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(default=0.00, verbose_name='Цена')
    publish_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-publish_date']
