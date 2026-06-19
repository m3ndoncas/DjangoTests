from django.contrib import admin

from .models import Poduto, Cliente

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClienteDados(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

admin.site.register(Poduto, ProdutoAdmin)
admin.site.register(Cliente, ClienteDados)
