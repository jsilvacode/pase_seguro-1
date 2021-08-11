# Generated by Django 3.2.6 on 2021-08-11 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadAcademica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField(verbose_name='horario de inicio')),
                ('hora_fin', models.TimeField(verbose_name='horario de término')),
                ('aula', models.CharField(max_length=100, verbose_name='aula / dependencia')),
                ('asignatura', models.CharField(max_length=100)),
                ('docente', models.CharField(max_length=200)),
                ('facultad', models.CharField(max_length=200)),
                ('carrera', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Actividad Académica',
                'verbose_name_plural': 'Actividades Académicas',
            },
        ),
        migrations.CreateModel(
            name='ActividadGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField(verbose_name='horario de inicio')),
                ('hora_fin', models.TimeField(verbose_name='horario de término')),
                ('dependencia', models.CharField(max_length=100, verbose_name='aula / dependencia')),
                ('descripcion', models.TextField(verbose_name='descripción / comentario')),
            ],
            options={
                'verbose_name': 'Actividad General',
                'verbose_name_plural': 'Actividades Generales',
            },
        ),
        migrations.CreateModel(
            name='AntecedentesAcademicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facultad', models.CharField(max_length=100)),
                ('carrera', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Antecedente Académico',
                'verbose_name_plural': 'Antecedentes Académicos',
                'ordering': ['facultad', 'carrera'],
            },
        ),
        migrations.CreateModel(
            name='AntecedentesPersonales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12, unique=True, verbose_name='RUT')),
                ('nombre', models.CharField(max_length=200, verbose_name='nombres')),
                ('apellido', models.CharField(max_length=200, verbose_name='apellidos')),
                ('email', models.EmailField(max_length=100, verbose_name='correo electrónico')),
                ('telefono', models.CharField(max_length=20, verbose_name='teléfono fijo / celular')),
            ],
            options={
                'verbose_name': 'Antecedente Personal',
                'verbose_name_plural': 'Antecedentes Personales',
            },
        ),
        migrations.CreateModel(
            name='AntecedentesSanitarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacto_estrecho', models.CharField(choices=[('sí', 'Sí'), ('no', 'No')], help_text='¿Ha tenido?.', max_length=10)),
                ('sintoma_fiebre', models.BooleanField(verbose_name='fiebre')),
                ('sintoma_perdida_olfato', models.BooleanField(verbose_name='pérdida del olfato')),
                ('sintoma_perdida_gusto', models.BooleanField(verbose_name='pérdida del gusto')),
                ('sintoma_tos', models.BooleanField(verbose_name='tos')),
                ('sintoma_dolor_garganta', models.BooleanField(verbose_name='dolor de garganta')),
                ('sintoma_secrecion_nasal', models.BooleanField(verbose_name='secreciones nasales')),
                ('sintoma_respiratorio', models.BooleanField(verbose_name='dificultad respiratoria')),
                ('sintoma_aumento_frecuencia', models.BooleanField(verbose_name='aumento de la frecuencia respiratoria')),
                ('sintoma_dolor_toracico', models.BooleanField(verbose_name='dolor torácico')),
                ('sintoma_dolor_muscular', models.BooleanField(verbose_name='dolor muscular')),
                ('sintoma_dolor_cabeza', models.BooleanField(verbose_name='dolor de cabeza')),
                ('sintoma_fatiga', models.BooleanField(verbose_name='fatiga')),
                ('sintoma_escalofrios', models.BooleanField(verbose_name='escalofríos')),
                ('sintoma_diarrea', models.BooleanField(verbose_name='diarrea')),
                ('sintoma_nausea_vomitos', models.BooleanField(verbose_name='náusea / vómitos')),
                ('sintoma_otro', models.CharField(blank=True, max_length=200, verbose_name='otros síntomas')),
                ('declaracion_confirmar', models.BooleanField(default=False, help_text='Aceptar.', verbose_name='declaración de salud idónea')),
                ('declaracion_archivo', models.FileField(blank=True, help_text='Doc adjunto.', upload_to='uploads/statements/%Y/%m/%d/', verbose_name='declaración de responsabilidad')),
            ],
            options={
                'verbose_name': 'Antecedente Sanitario',
                'verbose_name_plural': 'Antecedentes Sanitarios',
            },
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_ingreso', models.BooleanField(default=True)),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes')),
                ('actividad_general', models.ForeignKey(help_text='Actividades Generales (eventos).', on_delete=django.db.models.deletion.CASCADE, to='safepass.actividadgeneral', verbose_name='actividades generales')),
                ('antecedente_personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='safepass.antecedentespersonales', verbose_name='antecedentes personales')),
                ('antecedente_sanitario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='safepass.antecedentessanitarios', verbose_name='antecedentes sanitarios')),
            ],
            options={
                'verbose_name': 'Visita',
                'verbose_name_plural': 'Visitas',
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividad_academica', models.ForeignKey(help_text='Actividades Acádemicas (eventos).', on_delete=django.db.models.deletion.CASCADE, to='safepass.actividadacademica', verbose_name='actividades académicas')),
                ('antecedente_academico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='safepass.antecedentesacademicos', verbose_name='antecedentes académicos')),
                ('antecedente_personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='safepass.antecedentespersonales', verbose_name='antecedentes personales')),
                ('antecedente_sanitario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='safepass.antecedentessanitarios', verbose_name='antecedentes sanitarios')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
    ]
