# Generated by Django 2.1.3 on 2018-11-05 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0010_auto_20181103_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='estadoMascota',
            field=models.CharField(choices=[('Rescatado', 'Rescatado'), ('Disponible', 'Disponible'), ('Adoptado', 'Adoptado')], default='Rescatado', max_length=50, null=True),
        ),
    ]
