# Generated by Django 3.2 on 2023-05-16 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20230516_0957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelevents',
            old_name='sights',
            new_name='village',
        ),
    ]