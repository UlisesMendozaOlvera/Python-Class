# Generated by Django 4.1.2 on 2022-10-31 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automoviles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=255)),
                ('placas', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('linea', models.CharField(max_length=255)),
                ('modelo', models.CharField(max_length=255)),
                ('estatus', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Transportista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EquipoGPS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celular', models.IntegerField()),
                ('sim', models.IntegerField()),
                ('fabricante', models.CharField(max_length=255)),
                ('modelo', models.CharField(max_length=255)),
                ('estatus', models.CharField(max_length=255)),
                ('transportista', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Transportista.transportista')),
            ],
        ),
        migrations.CreateModel(
            name='AutomovilesEquipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaAsignacion', models.DateField()),
                ('fechaDesasignacion', models.DateField()),
                ('automoviles', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Transportista.automoviles')),
                ('transportista', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Transportista.transportista')),
            ],
        ),
        migrations.AddField(
            model_name='automoviles',
            name='transportista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Transportista.transportista'),
        ),
    ]
