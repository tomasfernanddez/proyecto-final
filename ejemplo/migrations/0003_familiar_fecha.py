# Generated by Django 4.1.3 on 2022-12-07 21:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0002_dummy'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='fecha',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]