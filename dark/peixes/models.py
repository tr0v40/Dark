from django.db import models
from mapas.models import Mapas


class Peixe(models.Model):
    mapa = models.ManyToManyField(Mapas)
    especie = models.CharField(max_length=128)
    trophy = models.IntegerField()
    super_trophy = models.IntegerField()
    temperatura_ideal = models.IntegerField()
    condicoes = models.CharField(max_length=128)
    time_list = models.CharField(max_length=128)
