from django.db import models

# Create your models here.
class Habilidades(models.Model):
    nome = models.CharField(max_length=128)
    tipo_pesca = models.BooleanField(default=False)


class SkillsPoints(models.Model):
    habilidades = models.ForeignKey(Habilidades, on_delete=models.CASCADE)
    nome = models.CharField(max_length=128)
    percentage_required = models.CharField(max_length=128)
    qtde_points = models.CharField(max_length=128)
    utility_level = models.CharField(max_length=128)
