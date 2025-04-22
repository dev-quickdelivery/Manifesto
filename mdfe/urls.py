from django.urls import path
from . import views

urlpatterns = [
    path('mdfe/manifesto/<int:manifesto_id>/em_transporte/', views.iniciar_manifesto, name='iniciar_manifesto'),
    path('mdfe/manifesto/<int:manifesto_id>/ver', views.ver_manifesto, name='ver_manifesto'),


]