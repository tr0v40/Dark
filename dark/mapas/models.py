from django.db import models
from skills.models import Habilidades


class Mapas(models.Model):
    nome = models.CharField(max_length=128)
    level = models.IntegerField()
    descricao = models.CharField(max_length=2048)
    habilidades = models.ForeignKey(Habilidades, on_delete=models.CASCADE)
