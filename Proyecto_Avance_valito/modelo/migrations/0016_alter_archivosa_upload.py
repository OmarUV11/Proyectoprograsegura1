# Generated by Django 4.0.4 on 2022-05-25 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0015_alter_archivosa_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivosa',
            name='upload',
            field=models.FileField(upload_to='Practicas/'),
        ),
    ]
