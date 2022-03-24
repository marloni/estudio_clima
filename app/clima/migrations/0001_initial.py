# Generated by Django 4.0.3 on 2022-03-24 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agnio', models.IntegerField(blank=True, null=True, verbose_name='Año')),
                ('glide', models.CharField(blank=True, max_length=50, null=True, verbose_name='Glide')),
                ('subgrupo_desastres', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subgrupo de Desastres')),
                ('tipo_desastre', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Desastre')),
                ('subtipo_desastre', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subtipo de Desastre')),
                ('nombre_evento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre del Evento')),
                ('pais', models.CharField(blank=True, max_length=50, null=True, verbose_name='País')),
                ('iso', models.CharField(blank=True, max_length=50, null=True, verbose_name='ISO')),
                ('region', models.CharField(blank=True, max_length=50, null=True, verbose_name='Región')),
                ('continente', models.CharField(blank=True, max_length=50, null=True, verbose_name='Continente')),
                ('ubicacion', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ubicación')),
                ('desastre_asociado', models.CharField(blank=True, max_length=50, null=True, verbose_name='Desastre asociado')),
                ('magnitud_desastre', models.CharField(blank=True, max_length=50, null=True, verbose_name='Magnitud del Desastre')),
                ('escala_desastre', models.CharField(blank=True, max_length=50, null=True, verbose_name='Escala del Desastre')),
                ('fecha_inicio', models.DateField(blank=True, help_text='Formato: dd/mm/yyyy', null=True, verbose_name='Fecha de Inicio')),
                ('fecha_finalizacion', models.DateField(blank=True, help_text='Formato: dd/mm/yyyy', null=True, verbose_name='Fecha de Finalización')),
                ('total_muertes', models.IntegerField(blank=True, null=True, verbose_name='Total de Muertes')),
                ('no_lesionados', models.IntegerField(blank=True, null=True, verbose_name='No. de Lesionados')),
                ('no_desaparecidos', models.IntegerField(blank=True, null=True, verbose_name='No. de Desaparecidos')),
                ('no_desmovilizados', models.IntegerField(blank=True, null=True, verbose_name='No. de Desmovilizados')),
                ('total_desaparecidos', models.IntegerField(blank=True, null=True, verbose_name='Total de Desaparecidos')),
                ('total_danos', models.IntegerField(blank=True, null=True, verbose_name='Total de Daños')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
                'ordering': ['agnio'],
            },
        ),
    ]
