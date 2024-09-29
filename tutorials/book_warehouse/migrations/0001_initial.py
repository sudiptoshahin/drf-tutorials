# Generated by Django 5.1.1 on 2024-09-29 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(max_length=100, unique=True)),
                ('url', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='book_warehouse.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=255, unique=True)),
                ('year', models.CharField(max_length=5)),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField(max_length=19)),
                ('author_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='book_author', to='book_warehouse.author')),
                ('publisher_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='book_publisher', to='book_warehouse.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_warehouse.customer')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='book_warehouse.shoppingbasket')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingBasket_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('book_isbn', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book_warehouse.book')),
                ('shopping_basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_warehouse.shoppingbasket')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('book_isbn', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book_warehouse.book')),
                ('warehouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book_warehouse.warehouse')),
            ],
        ),
    ]
