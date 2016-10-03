# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Departamento(models.Model):

    nombre = models.CharField('Nombre', max_length=255)
    cod_inei = models.CharField('Código INEI', max_length=10)
    cod_reniec = models.CharField('Código RENIEC', max_length=10, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        default_related_name = 'departamentos'

    def __str__(self):
        return self.nombre


@python_2_unicode_compatible
class Provincia(models.Model):

    departamento = models.ForeignKey('Departamento')

    nombre = models.CharField('Nombre', max_length=255)
    cod_inei = models.CharField('Código INEI', max_length=10)
    cod_reniec = models.CharField('Código RENIEC', max_length=10, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        default_related_name = 'provincias'

    def __str__(self):
        return self.nombre


@python_2_unicode_compatible
class Distrito(models.Model):

    provincia = models.ForeignKey('Provincia')

    nombre = models.CharField('Nombre', max_length=255)
    cod_inei = models.CharField('Código INEI', max_length=10)
    cod_reniec = models.CharField('Código RENIEC', max_length=10, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Distrito'
        verbose_name_plural = 'Distritos'
        default_related_name = 'distritos'

    def __str__(self):
        return self.nombre
