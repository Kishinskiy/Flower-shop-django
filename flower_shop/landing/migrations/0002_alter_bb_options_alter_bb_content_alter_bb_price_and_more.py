# Generated by Django 4.2 on 2023-05-01 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bb',
            options={'ordering': ['-publish_date'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterField(
            model_name='bb',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='price',
            field=models.FloatField(default=0.0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Товар'),
        ),
    ]
