from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Manifesto
from motorista.models import Motorista
from django.contrib import messages
from .utils import criar_manifesto
from datetime import datetime
from django.utils.formats import number_format
def iniciar_manifesto(request, manifesto_id):
    manifesto = get_object_or_404(Manifesto, id=manifesto_id)
    manifesto.viagem_inicio = datetime.now()
    manifesto.status = 'Em_transporte'  # ou o valor que você usa
    manifesto.save()
    messages.success(request, "Manifesto iniciado com sucesso.")
    return redirect('painel')  # redirecione para a lista de manifestos

@login_required
def ver_manifesto(request, manifesto_id):
    # Buscar a instância de Motorista associada ao usuário logado
    motorista = get_object_or_404(Motorista, user=request.user)
    # Busca manifesto do motorista
    manifesto = Manifesto.objects.all().get(id=manifesto_id, motorista=motorista)


    # Agora buscamos o manifesto, verificando se ele pertence ao motorista correto
    manifesto = Manifesto.objects.all().get(id=manifesto_id, motorista=motorista)

    if manifesto.status != 'Em_transporte':
        messages.warning(request, "Este manifesto ainda não está em transporte.")
        return redirect('painel')

        # Soma valores das notas (calculado na view, não salvo no DB)
    total_valor = 0
    if manifesto.dados:
        for nota in manifesto.dados:
            for produto in nota.get("produtos", []):
                total_valor += produto["ValorUnitario"] * produto["Quantidade"]

    # Soma valores de cada nota
    notas_valores = []

    for nota in manifesto.dados:
        total_nota = sum(p["ValorUnitario"] * p["Quantidade"] for p in nota.get("produtos", []))
        nota["total_nota"] = total_nota
        
            
    

    return render(request, 'manifesto/ver_manifesto.html', {
        'manifesto': manifesto,
        'total_valor': total_valor,
        'total_nota': total_nota
    })






