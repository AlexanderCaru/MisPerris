# Generated by Django 2.1.2 on 2018-11-03 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0007_auto_20181102_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(null=True, upload_to='media/imagesmascotas/'),
        ),
    ]