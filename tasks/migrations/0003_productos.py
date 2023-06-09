# Generated by Django 4.1.7 on 2023-03-11 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=255)),
                ('sku', models.CharField(max_length=255)),
                ('upc', models.CharField(max_length=255)),
                ('precio_usd', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('proveedor_sugerido', models.CharField(max_length=255)),
                ('arancel', models.DecimalField(decimal_places=2, max_digits=10)),
                ('check_importante', models.BooleanField()),
            ],
        ),
    ]
