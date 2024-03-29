# Generated by Django 3.2.7 on 2022-02-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_solution_solutiondocument_solutionelement'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='slug',
            field=models.SlugField(default='dd', max_length=150, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
