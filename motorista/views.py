from django.shortcuts import render
from django.http import JsonResponse
from .models import Motorista
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from motorista.models import Motorista
from django.contrib.auth.decorators import login_required

def verificar_cpf(request):
    if request.method == "POST":
        cpf = request.POST.get("cpf")
        motorista = Motorista.objects.filter(cpf=cpf).first()

        if motorista:
            if motorista.user:
                return JsonResponse({"status": "tem_usuario"})
            else:
                return JsonResponse({"status": "sem_usuario"})
        else:
            return JsonResponse({"status": "nao_encontrado"})


@login_required
def painel_view(request):
    return render(request, 'dashboard/painel.html')