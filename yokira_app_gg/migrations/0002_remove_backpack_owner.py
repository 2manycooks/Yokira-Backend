# Generated by Django 3.1.6 on 2021-02-11 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yokira_app_gg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backpack',
            name='owner',
        ),
    ]
