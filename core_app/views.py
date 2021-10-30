from django.shortcuts import render, get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader

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

    prod = get_object_or_404(Produto, id=pk)
    # prod = Produto.objects.get(id=pk)
    context = {
        'produto' : prod
    }
    return render(request,'produto.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    #return render(request, '404.html')
    print('teste')
    return HttpResponse(content=template.render(), content_type ='txt/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    # return render(request, '500.html')
    return HttpResponse(content=template.render(), content_type ='txt/html; charset=utf8', status=500)
