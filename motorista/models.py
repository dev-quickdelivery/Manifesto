from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

class Motorista(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    nome = models.CharField(max_length=100)
    mobile_person_id=models.CharField(max_length=100, null=True, blank=True)
    cnh = models.CharField(max_length=12, null=True, blank=True)
    placa = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.cpf}"

    
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
