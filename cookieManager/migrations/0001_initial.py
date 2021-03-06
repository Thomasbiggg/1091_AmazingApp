# Generated by Django 3.1.4 on 2021-01-02 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerID', models.IntegerField()),
                ('CustomerName', models.TextField()),
                ('Gender', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPurchaseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerID', models.IntegerField()),
                ('ProductID', models.IntegerField()),
                ('PurchaseQuantity', models.IntegerField()),
                ('PurchasePrice', models.IntegerField()),
                ('Comment', models.TextField()),
                ('Date', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MarketingIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerID', models.IntegerField()),
                ('ForecastPurchaseProb', models.DecimalField(decimal_places=2, max_digits=19)),
                ('CLV', models.DecimalField(decimal_places=2, max_digits=19)),
                ('WalletShare', models.DecimalField(decimal_places=2, max_digits=19)),
                ('CategaryDemandShare', models.DecimalField(decimal_places=2, max_digits=19)),
                ('ProportionofPositiveComment', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductID', models.IntegerField()),
                ('ProductName', models.TextField()),
                ('ProductPrice', models.DecimalField(decimal_places=2, max_digits=19)),
                ('InventoryAmount', models.IntegerField()),
            ],
        ),
    ]
