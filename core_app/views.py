from django.shortcuts import render
from .models import Produto

def index(request):
    produtos = Produto.objects.all()

    if str(request.user) == 'AnonymousUser':
        status_usuario = 'Usuário não logado'
    else:
        status_usuario = 'Usuário logado' #+ request.user.firstname
    context ={
        'curso' : 'Programação Web com Django',
        'produtos' : produtos,
        'status_usuario' : status_usuario
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    print(f'PK:{pk}')

    prod = Produto.objects.get(id=pk)
    context = {
        'produto' : prod
    }
    return render(request,' produto.html', context)