# Generated by Django 3.2.7 on 2021-10-08 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdocument',
            name='actif',
        ),
    ]