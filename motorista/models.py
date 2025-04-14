from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

class Motorista(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    nome = models.CharField(max_length=100)
    cnh = models.CharField(max_length=12, null=True, blank=True)
    placa = models.CharField(max_length=8, null=True, blank=True)

    
    def set_senha(self, senha):
        # Garante que só cria se ainda não tiver user vinculado
        if not self.user:
            user = User.objects.create_user(
                username=self.cpf,
                password=senha,
                first_name=self.nome
            )
            self.user = user
            self.save()
