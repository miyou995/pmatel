# Generated by Django 3.2.7 on 2021-10-10 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counter',
            name='before',
        ),
    ]
