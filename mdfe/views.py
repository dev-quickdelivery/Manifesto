from django.shortcuts import render, get_object_or_404, redirect
from .models import Manifesto
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