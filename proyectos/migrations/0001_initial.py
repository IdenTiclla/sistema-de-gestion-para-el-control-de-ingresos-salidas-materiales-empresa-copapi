# Generated by Django 4.2.1 on 2023-06-08 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'Barrio',
            },
        ),
        migrations.CreateModel(
            name='Encargado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('ci', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'Encargado',
            },
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'TipoServicio',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField(auto_now=True)),
                ('barrio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.barrio')),
                ('encargado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='proyectos.encargado')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.tiposervicio')),
            ],
            options={
                'db_table': 'Proyecto',
            },
        ),
    ]