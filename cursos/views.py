from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.template import loader
from django.http import HttpResponse

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
    #prod = Poduto.objects.get(id=id)
    prod = get_object_or_404(Poduto, id=id)
    context = {
        'p': prod
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)

