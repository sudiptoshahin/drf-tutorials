# Generated by Django 5.1.1 on 2024-09-25 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_attribute_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='text',
            field=models.CharField(default='hello', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
