from django.contrib import admin
from .models import  Manifesto , Transportadora
from django.urls import path
from django.utils.html import format_html

from django.urls import reverse


# mdfe/admin.py
from django.contrib import admin
from .models import Manifesto

@admin.register(Manifesto)
class ManifestoAdmin(admin.ModelAdmin):
    list_display = ('numero_rota', 'motorista', 'status')
    
    @admin.action(description='Iniciar transporte selecionado(s)')
    def iniciar_transporte(self, request, queryset):
        updated = queryset.update(status='Em_transporte')
        self.message_user(request, f'{updated} manifesto(s) iniciado(s) com sucesso.')



admin.site.register(Transportadora)