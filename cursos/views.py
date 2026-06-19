from django.shortcuts import render

from .models import Poduto

def index(request):
    produtos = Poduto.objects.all()
    context = {
        'curso': 'Programação web com Django',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    prod = Poduto.objects.get(id=id)
    context = {
        'p': prod
    }
    return render(request, 'produto.html', context)