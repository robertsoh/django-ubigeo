# -*- coding: utf-8 -*-
from .models import Provincia, Distrito


class UbigeoForm(object):
    """Declare chains of ubigeo fields"""

    ubigeo_chains = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for chain in self.ubigeo_chains:
            assert isinstance(chain, (tuple, list))
            assert len(chain) == 3, '3 fields are required'
            dep, pro, dis = chain
            # load empty select for new create forms
            self.fields[pro].queryset = Provincia.objects.none()
            self.fields[dis].queryset = Distrito.objects.none()
            if self._meta.model.objects.filter(id=self.instance.id).exists() and not self.data:
                # when exists a record and not POST data get queryset from instance
                self.fields[pro].queryset = getattr(self.instance, dep).provincias.all()
                self.fields[dis].queryset = getattr(self.instance, pro).distritos.all()
            else:
                self.fields[pro].queryset = Provincia.objects.filter(departamento_id=self.data.get(dep))
                self.fields[dis].queryset = Distrito.objects.filter(provincia_id=self.data.get(pro))
