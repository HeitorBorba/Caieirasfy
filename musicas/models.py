from django.db import models

# Create your models here.
from django.db.models import CharField


class Musicas(models.Model):
    Nome = models.CharField(
        max_length=50
    )
    Artista = models.CharField(
        max_length=50
    )
    Genero = models.CharField(
        max_length=50
    )
    Musical = models.CharField(
        max_length=50
    )
