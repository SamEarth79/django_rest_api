# Generated by Django 4.1.7 on 2023-05-18 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name of the show')),
                ('fav', models.CharField(max_length=50, verbose_name='Favourite Character')),
            ],
        ),
    ]
