# Generated by Django 3.2.4 on 2021-08-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='personal_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Phone_number', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=100)),
                ('State', models.CharField(choices=[('State No. 1', 'State No. 1'), ('State No. 2', 'State No. 2'), ('State No. 3', 'State No. 3'), ('State No. 4', 'State No. 4'), ('State No. 5', 'State No. 5'), ('State No. 6', 'State No. 6'), ('State No. 7', 'State No. 7')], max_length=200)),
                ('District', models.CharField(max_length=100)),
                ('municipality', models.CharField(max_length=200)),
                ('VDC', models.CharField(max_length=100)),
                ('Ward_No', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UploadsBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Name', models.CharField(max_length=200)),
                ('Author_Name', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('ReleaseDates', models.DateTimeField(auto_now_add=True)),
                ('Selling_price', models.FloatField()),
                ('Discount_price', models.FloatField(null=True)),
                ('Lable', models.CharField(choices=[('o', 'Old'), ('N', 'New')], max_length=2)),
                ('Publication', models.CharField(max_length=200)),
                ('Types_of_Book', models.CharField(choices=[('Action and Adventure', 'Action and Adventure'), ('Classics', 'Classics'), ('Comic Book or Graphic Novel', 'Comic Book or Graphic Novel.'), ('Detective and Mystery', 'Detective and Mystery'), ('Fantasy', 'Fantasy'), (' Historical Fiction', ' Historical Fiction'), ('Horror', ' Horror'), ('Literary Fiction', 'Literary Fiction'), ('School', 'School'), ('+2', '+2'), ('+2', '+2'), ('Bachelor', 'Bachelor'), ('Bachelor', 'Bachelor'), ('Master  and degree', 'Master  and degree'), ('Other', 'Others')], max_length=100)),
                ('Quantity', models.PositiveBigIntegerField(default=1)),
                ('Image', models.ImageField(upload_to='book_images/')),
            ],
        ),
    ]
