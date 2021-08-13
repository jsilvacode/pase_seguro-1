# Generated by Django 3.2.6 on 2021-08-13 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safepass', '0003_auto_20210812_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividadacademica',
            name='carrera',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='actividadacademica',
            name='docente',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='actividadacademica',
            name='facultad',
            field=models.CharField(choices=[('Facultad de Ciencias de la Salud', 'FACS'), ('Facultad de Educación y Ciencias Sociales', 'FECS'), ('Facultad de Ingeniería y Negocios', 'FAIN'), ('Facultad de Teología', 'FTEO')], max_length=100),
        ),
    ]