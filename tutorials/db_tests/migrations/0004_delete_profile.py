# Generated by Django 5.1.1 on 2024-10-01 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_tests', '0003_alter_profile_bio_alter_profile_birthdate_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
