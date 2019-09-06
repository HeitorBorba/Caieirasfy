from rest_framework import serializers

from musicas.models import Musicas


class MusicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musicas
        fields = ('Nome', 'Artista', 'Genero', 'Musical')