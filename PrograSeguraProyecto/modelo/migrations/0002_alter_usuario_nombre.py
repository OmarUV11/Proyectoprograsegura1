# Generated by Django 4.0.4 on 2022-05-08 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=25),
        ),
    ]