# Generated by Django 4.2.5 on 2023-09-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_account_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='Verified User'),
        ),
    ]
