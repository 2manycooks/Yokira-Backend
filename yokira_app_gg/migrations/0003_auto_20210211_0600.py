# Generated by Django 3.1.6 on 2021-02-11 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yokira_app_gg', '0002_remove_backpack_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enemyimage',
            name='image',
            field=models.ImageField(upload_to=None),
        ),
    ]
