# Generated by Django 4.2.5 on 2023-09-25 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mastertableconfig', '0001_initial'),
        ('user', '0002_account_created_at_account_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_masterconfig', to='mastertableconfig.masterconfig'),
        ),
    ]
