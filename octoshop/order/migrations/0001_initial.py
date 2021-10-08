# Generated by Django 3.2.7 on 2021-09-25 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('delivery', '0001_initial'),
        ('core', '0001_initial'),
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nom')),
                ('last_name', models.CharField(max_length=50, verbose_name='Prenom')),
                ('address', models.CharField(max_length=250, verbose_name='Adresse')),
                ('phone', models.CharField(max_length=25, verbose_name='Téléphone')),
                ('campany', models.CharField(blank=True, max_length=150, null=True, verbose_name='Entrprise')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Crée')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Modifié')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('paid', models.BooleanField(default=False, verbose_name='Payé')),
                ('confirmer', models.BooleanField(default=False, verbose_name='Confirmé')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Réduction')),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Prix Livraison')),
                ('commune', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='delivery.commune')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='coupons.coupon', verbose_name='Coupons')),
                ('wilaya', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='delivery.wilaya')),
            ],
            options={
                'verbose_name': 'Commande',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Prix')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantité')),
                ('attribute_1', models.CharField(blank=True, max_length=50, null=True, verbose_name='spécificité 1')),
                ('attribute_2', models.CharField(blank=True, max_length=50, null=True, verbose_name='spécificité 2')),
                ('attribute_3', models.CharField(blank=True, max_length=50, null=True, verbose_name='spécificité 3')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order', verbose_name='Commande')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product', verbose_name='Produit')),
            ],
        ),
    ]
