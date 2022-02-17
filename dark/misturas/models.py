from django.db import models
from mapas.models import Mapas
from peixes.models import Peixe


class Gb(models.Model):
    mapa = models.ManyToManyField(Mapas)
    peixes = models.ManyToManyField(Peixe)
    nome = models.CharField(max_length=128)
    base = models.CharField(max_length=128)
    aditivo1 = models.CharField(max_length=128)
    aditivo2 = models.CharField(max_length=128)
    aditivo3 = models.CharField(max_length=128)
    aditivo4 = models.CharField(max_length=128)
    engodo = models.CharField(max_length=128)


class MisturaSeca(models.Model):
    mistura = models.CharField(max_length=128)
    aditivo1 = models.CharField(max_length=128)
    aditivo2 = models.CharField(max_length=128)
    aditivo3 = models.CharField(max_length=128)
    aditivo4 = models.CharField(max_length=128)
    atrativo = models.CharField(max_length=128)


class Pva(models.Model):
    mapa = models.ManyToManyField(Mapas)
    peixes = models.ManyToManyField(Peixe)
    nome = models.CharField(max_length=128)
    mistura_seca = models.ForeignKey(MisturaSeca, on_delete=models.CASCADE)