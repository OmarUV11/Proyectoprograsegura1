# Generated by Django 3.2.13 on 2022-05-27 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0016_alter_archivosa_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='Estado_token',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='Contraseña',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='salt',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
