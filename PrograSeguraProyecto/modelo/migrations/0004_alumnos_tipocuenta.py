# Generated by Django 2.2.12 on 2022-05-10 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0003_auto_20220509_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='Tipocuenta',
            field=models.CharField(max_length=20, null=True),
        ),
    ]