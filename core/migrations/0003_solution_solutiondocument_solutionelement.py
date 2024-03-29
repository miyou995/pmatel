# Generated by Django 3.2.7 on 2022-02-06 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_productdocument_actif'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nom / titre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('actif', models.BooleanField(default=True, verbose_name='actif')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour')),
            ],
        ),
        migrations.CreateModel(
            name='SolutionElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nom / titre')),
                ('photo', models.ImageField(upload_to='images/solutions')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('actif', models.BooleanField(default=True, verbose_name='actif')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour')),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elements', to='core.solution')),
            ],
        ),
        migrations.CreateModel(
            name='SolutionDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='images/produits')),
                ('name', models.CharField(max_length=25, verbose_name='Nom du document')),
                ('actif', models.BooleanField(default=True, verbose_name='actif')),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='core.solution')),
            ],
        ),
    ]
