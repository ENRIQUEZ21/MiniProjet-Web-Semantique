# Generated by Django 3.2.8 on 2021-10-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversionCSVTTL', '0009_auto_20211027_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='prefix_subj',
        ),
        migrations.AddField(
            model_name='information',
            name='prefix_obj',
            field=models.CharField(default='d', max_length=25),
        ),
        migrations.AlterField(
            model_name='information',
            name='prefix_pred',
            field=models.CharField(default='p', max_length=25),
        ),
    ]
