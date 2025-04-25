from django.shortcuts import render
from django.http import JsonResponse
from .models import Motorista
from .utils import registrar_motoristas
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from motorista.models import Motorista
from mdfe.models import Manifesto
from django.contrib.auth.decorators import login_required
from mdfe.utils import criar_manifesto


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
    criar_manifesto()
    manifesto = Manifesto.objects.all()
    motorista = Motorista.objects.get(user=request.user)

    #pega todos os manifestos do motorista logado
    manifesto = manifesto.filter(motorista=motorista)



    context = {
        'manifesto': manifesto,        
        'motorista': motorista
    }

    return render(request, 'dashboard/painel.html', context)