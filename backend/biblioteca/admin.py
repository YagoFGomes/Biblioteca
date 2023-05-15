from django.contrib import admin
from biblioteca.models import *

# Register your models here.

admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(LivroFisico)
admin.site.register(Reserva)
admin.site.register(Leitor)