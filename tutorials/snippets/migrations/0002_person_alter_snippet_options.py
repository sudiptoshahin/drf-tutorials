# Generated by Django 5.1.1 on 2024-09-24 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First name', max_length=100)),
                ('last_name', models.CharField(help_text='Last name', max_length=100)),
                ('email', models.EmailField(help_text='Email', max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], help_text='Gender', max_length=6)),
            ],
        ),
        migrations.AlterModelOptions(
            name='snippet',
            options={},
        ),
    ]
