import json
from django.test import RequestFactory, TestCase

from django.urls import resolve

from ubigeo import views
from ubigeo.models import Departamento, Provincia, Distrito


class ProvinciaViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.view = views.ProvinciaView.as_view()
        self.lima = Departamento.objects.create(nombre='Lima', cod_inei='15')
        self.ica = Departamento.objects.create(nombre='Ica', cod_inei='11')
        Provincia.objects.create(departamento=self.lima, nombre='Lima', cod_inei='1501')
        Provincia.objects.create(departamento=self.ica, nombre='Ica', cod_inei='1101')

    def test_match_expected_view(self):
        url = resolve('/provincias/')
        self.assertEqual(url.func.__name__, self.view.__name__)

    def test_response_return_all_provincias(self):
        request = self.factory.get('/')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf8'))
        self.assertIn('data', data)
        self.assertEqual(len(data['data']), Provincia.objects.all().count())

    def test_response_return_filtered_provincies(self):
        request = self.factory.get('/?departamento_id=' + str(self.lima.id))
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf8'))
        self.assertIn('data', data)
        self.assertEqual(len(data['data']), Provincia.objects.filter(departamento_id=self.lima.id).count())


class DistritoViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.view = views.DistritoView.as_view()
        self.lima = Departamento.objects.create(nombre='Lima', cod_inei='15')
        self.ica = Departamento.objects.create(nombre='Ica', cod_inei='11')
        self.provincia_lima = Provincia.objects.create(departamento=self.lima, nombre='Lima', cod_inei='1501')
        self.provincia_ica = Provincia.objects.create(departamento=self.ica, nombre='Ica', cod_inei='1101')
        Distrito.objects.create(nombre='Lima', provincia=self.provincia_lima, cod_inei='150101')
        Distrito.objects.create(nombre='Ica', provincia=self.provincia_ica, cod_inei='110101')

    def test_match_expected_view(self):
        url = resolve('/distritos/')
        self.assertEqual(url.func.__name__, self.view.__name__)

    def test_response_return_all_distritos(self):
        request = self.factory.get('/')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf8'))
        self.assertIn('data', data)
        self.assertEqual(len(data['data']), Distrito.objects.all().count())

    def test_response_return_filtered_distritos(self):
        request = self.factory.get('/?provincia_id=' + str(self.provincia_lima.id))
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf8'))
        self.assertIn('data', data)
        self.assertEqual(len(data['data']), Distrito.objects.filter(provincia_id=self.provincia_lima.id).count())
