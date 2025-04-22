from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Manifesto 
from motorista.models import Motorista
from django.contrib import messages
from .utils import iniciar_transporte_api, finalizar_transporte_api

def iniciar_transporte(request, manifesto_id):
    manifesto = get_object_or_404(Manifesto, id=manifesto_id)
    manifesto.status = 'em_transporte'
    manifesto.save()
    iniciar_transporte_api(manifesto.id)  # Simulação da API
    return redirect('admin:index')

def finalizar_transporte(request, manifesto_id):
    manifesto = get_object_or_404(Manifesto, id=manifesto_id)
    manifesto.status = 'finalizado'
    manifesto.save()
    finalizar_transporte_api(manifesto.id)  # Simulação da API
    return redirect('admin:index')

def iniciar_manifesto(request, manifesto_id):
    manifesto = get_object_or_404(Manifesto, id=manifesto_id)
    manifesto.status = 'Em_transporte'  # ou o valor que você usa
    manifesto.save()
    messages.success(request, "Manifesto iniciado com sucesso.")
    return redirect('painel')  # redirecione para a lista de manifestos


@login_required
def ver_manifesto(request, manifesto_id):
    # Buscar a instância de Motorista associada ao usuário logado
    motorista = get_object_or_404(Motorista, user=request.user)

    # Agora buscamos o manifesto, verificando se ele pertence ao motorista correto
    manifesto = Manifesto.objects.all().get(id=manifesto_id, motorista=motorista)

    if manifesto.status != 'Em_transporte':
        messages.warning(request, "Este manifesto ainda não está em transporte.")
        return redirect('painel')

    return render(request, 'manifesto/ver_manifesto.html', {
        'manifesto': manifesto,
        'notas': manifesto.notas.all()  # ou o nome correto do related_name se estiver definido
    })



