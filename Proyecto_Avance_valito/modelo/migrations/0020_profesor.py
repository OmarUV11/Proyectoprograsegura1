# Generated by Django 3.2.13 on 2022-06-06 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0019_archivosp_nombreactividad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreProfesor', models.CharField(max_length=50)),
                ('Matricula', models.CharField(max_length=20)),
                ('Contraseña', models.CharField(max_length=100)),
                ('Tipocuenta', models.CharField(max_length=20, null=True)),
                ('Chat_id', models.CharField(max_length=40, null=True)),
                ('Token_tel', models.CharField(max_length=60, null=True)),
                ('Token_Env', models.CharField(max_length=60, null=True)),
                ('Token_Tem', models.DateTimeField(null=True)),
                ('salt', models.CharField(default='', max_length=100, null=True)),
                ('Estado_token', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]