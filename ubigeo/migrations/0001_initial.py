# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name=b'Nombre')),
                ('cod_inei', models.CharField(max_length=10, verbose_name=b'C\xc3\xb3digo INEI')),
                ('cod_reniec', models.CharField(max_length=10, null=True, verbose_name=b'C\xc3\xb3digo RENIEC')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'default_related_name': 'departamentos',
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name=b'Nombre')),
                ('cod_inei', models.CharField(max_length=10, verbose_name=b'C\xc3\xb3digo INEI')),
                ('cod_reniec', models.CharField(max_length=10, null=True, verbose_name=b'C\xc3\xb3digo RENIEC')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Distrito',
                'verbose_name_plural': 'Distritos',
                'default_related_name': 'distritos',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name=b'Nombre')),
                ('cod_inei', models.CharField(max_length=10, verbose_name=b'C\xc3\xb3digo INEI')),
                ('cod_reniec', models.CharField(max_length=10, null=True, verbose_name=b'C\xc3\xb3digo RENIEC')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provincias', to='ubigeo.Departamento')),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
                'default_related_name': 'provincias',
            },
        ),
        migrations.AddField(
            model_name='distrito',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distritos', to='ubigeo.Provincia'),
        ),
    ]
