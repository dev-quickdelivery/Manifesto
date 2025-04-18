from django.contrib import admin
from .models import  Manifesto, Nota, Canhoto
from django.urls import path
from django.utils.html import format_html
from .views import iniciar_transporte, finalizar_transporte

class ManifestoAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'criado_em', 'acoes']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:manifesto_id>/iniciar/', self.admin_site.admin_view(iniciar_transporte), name='iniciar_transporte'),
            path('<int:manifesto_id>/finalizar/', self.admin_site.admin_view(finalizar_transporte), name='finalizar_transporte'),
        ]
        return custom_urls + urls

    def acoes(self, obj):
        return format_html(
            '<a class="button" href="{}">Iniciar</a> <a class="button" href="{}">Finalizar</a>',
            f"/admin/app/manifesto/{obj.id}/iniciar/",
            f"/admin/app/manifesto/{obj.id}/finalizar/",
        )
    acoes.short_description = 'Ações'
    acoes.allow_tags = True


admin.site.register(Manifesto, ManifestoAdmin)
admin.site.register(Nota)
admin.site.register(Canhoto)
