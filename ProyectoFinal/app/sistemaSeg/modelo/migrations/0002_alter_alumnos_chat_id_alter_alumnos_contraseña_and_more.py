# Generated by Django 4.0.1 on 2022-06-07 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='Chat_id',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='Contraseña',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='Matricula',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='NombreAlumno',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='Tipocuenta',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
