from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.

from musicas.models import Musicas
from musicas.serializers import MusicasSerializer
from rest_framework.filters import SearchFilter
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MusicasViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^Nome', '^Artista', '=Genero','^Musical']
    queryset = Musicas.objects.all()
    serializer_class = MusicasSerializer