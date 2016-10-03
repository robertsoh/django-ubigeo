# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Departamento, Provincia, Distrito


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'cod_inei', 'cod_reniec')
    search_fields = ('nombre', 'cod_inei', 'cod_reniec')


@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'cod_inei', 'cod_reniec')
    search_fields = ('nombre', 'cod_inei', 'cod_reniec')
    list_filter = ('departamento',)


@admin.register(Distrito)
class DistritoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'cod_inei', 'cod_reniec')
    search_fields = ('nombre', 'cod_inei', 'cod_reniec')
    list_filter = ('provincia',)
