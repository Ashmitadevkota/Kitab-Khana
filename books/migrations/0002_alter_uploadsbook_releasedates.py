# Generated by Django 3.2.4 on 2021-08-08 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadsbook',
            name='ReleaseDates',
            field=models.DateTimeField(),
        ),
    ]
