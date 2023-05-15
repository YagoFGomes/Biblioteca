from django.contrib.auth.models import User, Group
from biblioteca.models import *

from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ['url', 'nome', 'descricao']

class LivroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Livro
        fields = ['url', 'titulo', 'idioma', 'ano_publicacao', 'autor']

class LivroFisicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LivroFisico
        fields = ['url', 'status', 'codigo_barras', 'ref_livro' ]

class ReservaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reserva
        fields = ['url', 'data_reserva', 'reservado_ate', 'data_devolucao', 'status_reserva' ]

class LeitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leitor
        fields = ['url', 'nome', 'contato', 'email', 'tipo_documento', 'documento' ]