# Generated by Django 4.2 on 2023-05-08 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_rubric_bb_rubric'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
