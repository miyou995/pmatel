# Generated by Django 3.2.7 on 2021-10-10 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_remove_counter_before'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counter',
            name='icon',
        ),
    ]
