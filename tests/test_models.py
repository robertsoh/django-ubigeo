#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase

from ubigeo.models import Departamento, Provincia, Distrito


class DepartamentoTestCase(TestCase):

    def test_correct_creation(self):
        obj = Departamento.objects.create(
            nombre='Lima',
            cod_inei='01'
        )
        self.assertIsNotNone(obj)


class ProvinciaTestCase(TestCase):

    def setUp(self):
        self.departamento = Departamento.objects.create(
            nombre='Lima',
            cod_inei='01'
        )

    def test_correct_creation(self):
        obj = Provincia.objects.create(
            departamento=self.departamento,
            nombre='Lima',
            cod_inei='0101'
        )
        self.assertIsNotNone(obj)


class DistritoTestCase(TestCase):

    def setUp(self):
        self.departamento = Departamento.objects.create(
            nombre='Lima',
            cod_inei='01',
        )
        self.provincia = Provincia.objects.create(
            departamento=self.departamento,
            nombre='Lima',
            cod_inei='0101'
        )

    def test_correct_creation(self):
        obj = Distrito.objects.create(
            provincia=self.provincia,
            nombre='Lima',
            cod_inei='010101'
        )
        self.assertIsNotNone(obj)
