from django.db import models
from biblioteca.utils import lista_idiomas, status_livro, status_reserva, tipo_documento

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self) -> str:
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=300)
    idioma = models.CharField(max_length=50, choices=lista_idiomas)
    ano_publicacao = models.DateField(blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.titulo

class LivroFisico(models.Model):
    status = models.CharField(max_length=50, choices=status_livro)
    codigo_barras = models.CharField(max_length=50)
    ref_livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.ref_livro} - {self.ref_livro}'


class Leitor(models.Model):
    nome = models.CharField(max_length=300)
    contato = models.CharField(max_length=15)
    email = models.EmailField()
    tipo_documento = models.CharField(max_length=50, choices=tipo_documento )
    documento = models.CharField(max_length=50)


class Reserva(models.Model):
    codigo_reserva = models.CharField(max_length=50)
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    data_reserva = models.DateField(auto_created=True)
    reservado_ate = models.DateField()
    data_devolucao = models.DateField(blank=True, null=True)
    status_reserva = models.CharField(max_length=50, choices=status_reserva)

    def __str__(self) -> str:
        return self.titulo