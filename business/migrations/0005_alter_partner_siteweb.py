# Generated by Django 3.2.7 on 2021-10-10 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20211010_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='siteweb',
            field=models.URLField(blank=True, max_length=250, null=True, verbose_name='Lien'),
        ),
    ]