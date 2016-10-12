# -*- coding: utf-8 -*-
from django.views.generic import View
from django.http import JsonResponse

from .models import Provincia, Distrito


class UbigeoView(View):

    model = None
    parent_field = None

    def get(self, request, *args, **kwargs):
        data = []
        params = {}
        if self.parent_field in request.GET:
            params[self.parent_field] = request.GET.get(self.parent_field)
        for obj in self.model.objects.filter(**params):
            data.append({
                'id': obj.id,
                'nombre': obj.nombre,
                'cod_inei': obj.cod_inei,
                'cod_reniec': obj.cod_reniec
            })
        return JsonResponse({'data': data})


class ProvinciaView(UbigeoView):

    model = Provincia
    parent_field = 'departamento_id'


class DistritoView(UbigeoView):

    model = Distrito
    parent_field = 'provincia_id'
