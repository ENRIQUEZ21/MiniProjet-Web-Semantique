# Generated by Django 3.2.8 on 2021-10-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversionCSVTTL', '0005_auto_20211026_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='delimitation',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
