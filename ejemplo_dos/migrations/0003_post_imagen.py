# Generated by Django 4.1.3 on 2023-01-05 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo_dos', '0002_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='posteos'),
        ),
    ]