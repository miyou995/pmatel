# Generated by Django 3.2.7 on 2021-10-10 08:57

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Nom de l'entreprise")),
                ('logo', models.ImageField(upload_to='images/logos', verbose_name='Logo')),
                ('logo_negatif', models.ImageField(upload_to='images/slides', verbose_name='Logo négatif')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Titre')),
                ('adress', models.CharField(blank=True, max_length=50, verbose_name='Adresse')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name="email de l'entreprise")),
                ('email2', models.EmailField(blank=True, max_length=50, verbose_name="2eme email de l'entreprise")),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name="numéro de téléphone de l'entreprise")),
                ('phone2', models.CharField(blank=True, max_length=50, verbose_name="2eme numéro de téléphone de l'entreprise")),
                ('about', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text a propos')),
                ('about_photo', models.ImageField(blank=True, null=True, upload_to='slides/', verbose_name='Photo A propos 440 X 275 px')),
                ('facebook', models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien page Facebook')),
                ('insta', models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien page Instagram')),
                ('twitter', models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien Compte Twitter')),
                ('linkedin', models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien Compte Linkedin')),
                ('youtube', models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien Chaine Youtube')),
                ('chat_code', models.TextField(blank=True, null=True, verbose_name='Script messagerie instantané')),
                ('pixel', models.TextField(blank=True, null=True, verbose_name='Script Facebook pixel')),
                ('analytics', models.TextField(blank=True, null=True, verbose_name='Script Analytics')),
                ('contact_message', models.TextField(blank=True, null=True, verbose_name='Contact message')),
                ('google_maps', models.TextField(blank=True, null=True, verbose_name='iframe google maps')),
            ],
            options={
                'verbose_name': '1. Infomation',
                'verbose_name_plural': '1. Infomations',
            },
        ),
        migrations.CreateModel(
            name='ClientService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name="nom de l'acomplissement")),
                ('sub_title', models.CharField(max_length=150, verbose_name="nom de l'acomplissement")),
                ('icon', models.ImageField(upload_to='icons/', verbose_name='icon 67 X 57 px ')),
                ('actif', models.BooleanField(default=True, verbose_name='actif')),
            ],
            options={
                'verbose_name': '7. Process PMATEL page a propos',
                'verbose_name_plural': '7. Process PMATEL page a propos',
            },
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name="nom de l'acomplissement")),
                ('before', models.CharField(blank=True, max_length=50, null=True, verbose_name='avant le chiffre')),
                ('number', models.IntegerField(verbose_name='chiffre')),
                ('icon', models.ImageField(upload_to='icons/', verbose_name='icon')),
                ('actif', models.BooleanField(default=True, verbose_name='actif')),
            ],
            options={
                'verbose_name': '6. Compteur',
                'verbose_name_plural': '6. Compteur',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250, verbose_name='Question')),
                ('reponse', models.TextField(verbose_name='Réponse')),
                ('actif', models.BooleanField(default=True, verbose_name='actif')),
            ],
        ),
        migrations.CreateModel(
            name='ThreePhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='slides/', verbose_name='photo 370 X 225 px')),
                ('url', models.URLField(verbose_name='lien')),
            ],
            options={
                'verbose_name': '3. Promotions Photos Acceuil',
                'verbose_name_plural': '3. Promotions Photos Acceuil',
            },
        ),
        migrations.CreateModel(
            name='LargeBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='slides/', verbose_name='Slide 1170 X 400 px')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Grand titre de la photo')),
                ('url', models.URLField(max_length=250, verbose_name='Lien')),
            ],
            options={
                'verbose_name': "5. Grand Banner bas de page d'accueil",
                'verbose_name_plural': "5. Grand Banner bas de d'accueil",
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='icons/', verbose_name='icon')),
                ('siteweb', models.URLField(max_length=250, verbose_name='Lien')),
                ('actif', models.BooleanField(default=True, verbose_name='actif')),
            ],
            options={
                'verbose_name': '9. Notre Partenaire / client',
                'verbose_name_plural': '9. Nos Partenaires / clients',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='slides/', verbose_name='Slide 870 X 475 px')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Grand titre de la photo')),
                ('sub_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sous titre de la photo')),
                ('url', models.URLField(max_length=250, verbose_name='Lien')),
                ('actif', models.BooleanField(default=True, verbose_name='actif')),
            ],
            options={
                'verbose_name': "2. Slides haut page d'accueil",
                'verbose_name_plural': "2. Slides haut page d'accueil",
            },
        ),
    ]