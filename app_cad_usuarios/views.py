from django.shortcuts import render
from .models import Usuario


def home(request):
    return render(request, 'usuarios/home.html')


def usuarios(request):
    # Salvando dados da tela para o DB
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # Mostrar usuarios cadastrados na pagina nova
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Voltar os dados para a listagem de usuarios na pagina
    return render(request, 'usuarios/usuarios.html', usuarios)
