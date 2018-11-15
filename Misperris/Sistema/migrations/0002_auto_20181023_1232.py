# Generated by Django 2.1.2 on 2018-10-23 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personamascota',
            name='Mascota',
        ),
        migrations.RemoveField(
            model_name='personamascota',
            name='Persona',
        ),
        migrations.AddField(
            model_name='mascota',
            name='Persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Sistema.Persona'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='codigoPersona',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='PersonaMascota',
        ),
    ]
