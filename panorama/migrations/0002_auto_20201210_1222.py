# Generated by Django 3.1.4 on 2020-12-10 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panorama', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panoramapost',
            name='image_origin_name',
            field=models.CharField(max_length=200),
        ),
    ]
