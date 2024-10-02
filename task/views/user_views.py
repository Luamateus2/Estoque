from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import messages
from ..models import Usuario


def autenticar_usuario(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            print('autenticado')
            return redirect(reverse('home'))
        else:
            messages.error(request, "Email ou senha incorreto.")
            return render(request, 'tasks/login.html')

    return render(request, 'tasks/login.html')

def adicionar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmar_senha = request.POST.get('confirmar_senha')

        if password != confirmar_senha:
            messages.error(request, "As senhas não correspondem.")
            return render(request, 'tasks/cadastro.html')

        Usuario = get_user_model()

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está em uso.")
            return render(request, 'tasks/cadastro.html')

        try:
            novo_usuario = Usuario.objects.create_user(
                email=email, nome=nome, password=password)
            messages.success(
                request, "Usuário criado com sucesso! Faça login para continuar.")
            return render(request,'tasks/login.html')
        except Exception as e:
            messages.error(
                request, "Ocorreu um erro ao criar o usuário. Tente novamente.")
            return render(request, 'tasks/cadastro.html')
    else:
        return render(request, 'tasks/cadastro.html')
