# Generated by Django 2.2.12 on 2022-05-09 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0002_alter_usuario_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreAlumno', models.CharField(max_length=50)),
                ('Matricula', models.CharField(max_length=20)),
                ('Contraseña', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
