from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=100, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    image  = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    price = models.FloatField(default=0.00, verbose_name='Цена')
    publish_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-publish_date']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
