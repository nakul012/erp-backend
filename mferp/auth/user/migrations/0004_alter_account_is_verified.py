# Generated by Django 4.2.5 on 2023-09-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_account_first_name_account_is_verified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_verified',
            field=models.BooleanField(default=True, verbose_name='Verified User'),
        ),
    ]