# Generated by Django 3.2.8 on 2021-10-25 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conversionCSVTTL', '0002_delete_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CSVfile', models.FileField(upload_to='')),
                ('delimitation', models.CharField(max_length=1)),
                ('if_title', models.BooleanField()),
                ('title_row', models.IntegerField()),
                ('start_row', models.IntegerField()),
                ('end_row', models.IntegerField()),
            ],
        ),
    ]
