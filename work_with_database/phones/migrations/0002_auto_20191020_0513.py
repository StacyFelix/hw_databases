# Generated by Django 2.2.6 on 2019-10-20 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateField(default='2019-10-20'),
        ),
    ]
