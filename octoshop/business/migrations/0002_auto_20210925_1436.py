# Generated by Django 3.2.7 on 2021-09-25 13:36

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
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
                'verbose_name': '7. Service Clients',
                'verbose_name_plural': '7. Services Clients',
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
                'verbose_name': '6. Accomplissement',
                'verbose_name_plural': '6. Accomplissement',
            },
        ),
        migrations.CreateModel(
            name='DualBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='slides/', verbose_name='photo 570 X 200 px')),
                ('url', models.URLField(verbose_name='lien')),
                ('actif', models.BooleanField(default=True, verbose_name='actif')),
            ],
            options={
                'verbose_name': '4. Petits Banners en duo',
                'verbose_name_plural': '4. Petits Banners en duo',
            },
        ),
        migrations.CreateModel(
            name='LargeBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='slides/', verbose_name='Slide 1170 X 400 px')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Grand titre de la photo')),
                ('sub_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sous titre de la photo')),
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
                'verbose_name': '9. Nos Partenaires',
                'verbose_name_plural': '9. Nos Partenaires',
            },
        ),
        migrations.CreateModel(
            name='Realisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name="nom de l'acomplissement")),
                ('description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Déscription du produit')),
                ('actif', models.BooleanField(default=True, verbose_name='actif')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour')),
            ],
            options={
                'verbose_name': '8. Nos Projets',
                'verbose_name_plural': '8. Nos Projets',
            },
        ),
        migrations.CreateModel(
            name='RealisationPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='icons/', verbose_name='icon')),
                ('actif', models.BooleanField(default=True, verbose_name='actif')),
                ('realisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.realisation', verbose_name='Projet / Réalisation')),
            ],
            options={
                'verbose_name': '9. Photos de Nos Projets',
                'verbose_name_plural': '9. Photos de Nos Projets',
            },
        ),
        migrations.CreateModel(
            name='ThreePhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='slides/', verbose_name='photo 370 X 225 px')),
                ('url', models.URLField(verbose_name='lien')),
            ],
            options={
                'verbose_name': '3. Trois Photos Acceuil',
                'verbose_name_plural': '3. Trois Photos Acceuil',
            },
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.AlterModelOptions(
            name='business',
            options={'verbose_name': '1. Infomation', 'verbose_name_plural': '1. Infomations'},
        ),
        migrations.AlterModelOptions(
            name='slide',
            options={'verbose_name': "2. Slides haut page d'accueil", 'verbose_name_plural': "2. Slides haut page d'accueil"},
        ),
        migrations.AddField(
            model_name='business',
            name='about_photo',
            field=models.ImageField(blank=True, null=True, upload_to='slides/', verbose_name='Photo A propos 440 X 275 px'),
        ),
        migrations.AddField(
            model_name='business',
            name='analytics',
            field=models.TextField(blank=True, null=True, verbose_name='Script Analytics'),
        ),
        migrations.AddField(
            model_name='business',
            name='chat_code',
            field=models.TextField(blank=True, null=True, verbose_name='Script messagerie instantané'),
        ),
        migrations.AddField(
            model_name='business',
            name='contact_message',
            field=models.TextField(blank=True, null=True, verbose_name='Contact message'),
        ),
        migrations.AddField(
            model_name='business',
            name='email2',
            field=models.EmailField(blank=True, max_length=50, verbose_name="2eme email de l'entreprise"),
        ),
        migrations.AddField(
            model_name='business',
            name='google_maps',
            field=models.TextField(blank=True, null=True, verbose_name='iframe google maps'),
        ),
        migrations.AddField(
            model_name='business',
            name='google_plus',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien Compte Google plus'),
        ),
        migrations.AddField(
            model_name='business',
            name='phone2',
            field=models.CharField(blank=True, max_length=50, verbose_name="2eme numéro de téléphone de l'entreprise"),
        ),
        migrations.AddField(
            model_name='business',
            name='pixel',
            field=models.TextField(blank=True, null=True, verbose_name='Script Facebook pixel'),
        ),
        migrations.AddField(
            model_name='business',
            name='twitter',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien Compte Twitter'),
        ),
        migrations.AddField(
            model_name='business',
            name='youtube',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien Chaine Youtube'),
        ),
        migrations.AddField(
            model_name='slide',
            name='actif',
            field=models.BooleanField(default=True, verbose_name='actif'),
        ),
        migrations.AddField(
            model_name='slide',
            name='sub_title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Sous titre de la photo'),
        ),
        migrations.AddField(
            model_name='slide',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Grand titre de la photo'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='photo',
            field=models.ImageField(upload_to='slides/', verbose_name='Slide 870 X 475 px'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='url',
            field=models.URLField(max_length=250, verbose_name='Lien'),
        ),
    ]
