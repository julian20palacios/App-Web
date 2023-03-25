# Generated by Django 4.1.7 on 2023-03-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('tax_id', models.CharField(max_length=50)),
                ('credit_limit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=20)),
                ('website', models.URLField()),
                ('delivery_method', models.CharField(max_length=100)),
                ('potential_brand', models.CharField(max_length=100)),
                ('potential_category', models.CharField(max_length=100)),
                ('price_opportunity', models.CharField(max_length=10)),
                ('featured_products', models.TextField()),
                ('credit_check', models.BooleanField(default=False)),
                ('document_check', models.BooleanField(default=False)),
                ('factoring_check', models.BooleanField(default=False)),
                ('is_important', models.BooleanField(default=False)),
                ('is_purchased', models.BooleanField(default=False)),
            ],
        ),
    ]