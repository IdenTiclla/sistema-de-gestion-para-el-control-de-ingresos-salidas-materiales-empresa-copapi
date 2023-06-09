# Generated by Django 4.2.1 on 2023-06-08 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('licencia', models.CharField(max_length=50)),
                ('ci', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Chofer',
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Vehiculo',
            },
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now=True)),
                ('chofer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transportes.chofer')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transportes.vehiculo')),
            ],
            options={
                'db_table': 'Transporte',
            },
        ),
    ]
