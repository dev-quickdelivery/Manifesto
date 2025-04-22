from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, PrimeiroAcessoForm
from motorista.models import Motorista
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse

def login_view(request):
    if request.user.is_authenticated:
        return redirect('painel')  # Usuário já logado, redireciona para o painel

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            senha = form.cleaned_data['senha']
            user = authenticate(username=cpf, password=senha)
            if user:
                auth_login(request, user)  # Isso mantém o usuário logado
                # Redireciona para a página que o usuário estava tentando acessar
                return redirect(request.GET.get('next', 'painel'))
            else:
                form.add_error(None, "CPF ou senha incorretos.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
    


def primeiro_acesso(request):
    if request.method == "POST":
        cpf = request.POST.get("cpf")
        senha = request.POST.get("senha")

        motorista = Motorista.objects.filter(cpf=cpf, user__isnull=True).first()
        if motorista:
            # Cria usuário com o CPF como username
            user = User.objects.create_user(username=cpf, password=senha)
            motorista.user = user
            motorista.save()
            return JsonResponse({"status": "ok"})
        else:
            return JsonResponse({"status": "erro", "mensagem": "Motorista não encontrado ou já possui conta"})
    return JsonResponse({"status": "erro", "mensagem": "Método inválido"})

# rota de logout
def logout_view(request):
    auth_logout(request)
    return redirect('login')


