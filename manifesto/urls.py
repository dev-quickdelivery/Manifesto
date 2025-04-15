"""
URL configuration for manifesto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import login_view, primeiro_acesso
from motorista.views import painel_view, verificar_cpf


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('painel/', painel_view, name='painel'),  # sua view após login
    path('verificar-cpf/', verificar_cpf, name='verificar_cpf'),
    path('primeiro-acesso/', primeiro_acesso, name='primeiro_acesso'),
    path('logout/', logout_view, name='logout'),
]
