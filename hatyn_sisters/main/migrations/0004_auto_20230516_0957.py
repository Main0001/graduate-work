# Generated by Django 3.2 on 2023-05-16 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_modelevents_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelevents',
            name='draft',
            field=models.BooleanField(default=True, verbose_name='Черновик'),
        ),
        migrations.AlterField(
            model_name='modelevents',
            name='sights',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.modelvillages', verbose_name='Достопримечательность'),
        ),
    ]
