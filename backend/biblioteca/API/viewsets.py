from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from biblioteca.API.serializer import *
from rest_framework.authentication import TokenAuthentication, BasicAuthentication


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]  
    permission_classes = [permissions.IsAuthenticated]

class AutorViewSet(viewsets.ModelViewSet):

    queryset = Autor.objects.all().order_by('nome')
    serializer_class = AutorSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class LivroViewSet(viewsets.ModelViewSet):

    queryset = Livro.objects.all().order_by('titulo')
    serializer_class = LivroSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class LivroFisicoViewSet(viewsets.ModelViewSet):

    queryset = LivroFisico.objects.all()
    serializer_class = LivroFisicoSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ReservaViewSet(viewsets.ModelViewSet):

    queryset = Reserva.objects.all().order_by('data_reserva')
    serializer_class = ReservaSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class LeitorViewSet(viewsets.ModelViewSet):

    queryset = Leitor.objects.all().order_by('nome')
    serializer_class = LeitorSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]