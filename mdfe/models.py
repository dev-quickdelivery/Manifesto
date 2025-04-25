from django.db import models
from motorista.models import Motorista
import datetime

# Modelo Transportadora
class Transportadora(models.Model):
    codigo = models.CharField(max_length=100)
    razao = models.CharField(max_length=200)

    def __str__(self):
        return self.razao
    
# Modelo Endereço
class Endereco(models.Model):
    nome = models.CharField(max_length=200)
    rua = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    pais = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=20)
    cnpj_matriz = models.CharField(max_length=20)
    tipo_matriz = models.CharField(max_length=20)
    codigo_ibge = models.CharField(max_length=10)
    posicao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.cidade}"
    
# Modelo Manifesto
class Manifesto(models.Model):
    STATUS_CHOICES = [
        ('Aguardando_Motorista', 'Aguardando'),
        ('Em_transporte', 'Em Transporte'),
        ('Finalizado', 'Finalizado'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Aguardando_Motorista', blank=True, null=True)
    numero_rota = models.CharField(max_length=100 ,blank=True, null=True)
    rota_destino = models.CharField(max_length=200,blank=True, null=True)
    rota_nome = models.CharField(max_length=200 ,blank=True, null=True)
    data = models.DateTimeField(default=datetime.datetime.now ,blank=True, null=True)
    viagem_inicio = models.DateTimeField(blank=True, null=True)
    viagem_fim = models.DateTimeField(blank=True, null=True)
    regiao = models.CharField(max_length=100 ,blank=True, null=True)
    transportadora = models.ForeignKey(Transportadora, on_delete=models.CASCADE ,blank=True, null=True)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    origem = models.CharField(max_length=100,blank=True, null=True)
    destino = models.CharField(max_length=100,blank=True, null=True)
    limites_inicio = models.DateTimeField(blank=True, null=True)
    limites_fim = models.DateTimeField(blank=True, null=True)
    tipo_rota = models.CharField(max_length=1, choices=[('D', 'D'), ('T', 'T'), ('P', 'P'), ('R', 'R')],blank=True, null=True)
    tipo_material = models.CharField(max_length=100,blank=True, null=True)
    fornecimento = models.CharField(max_length=100,blank=True, null=True)
    tipo_frete = models.CharField(max_length=100,blank=True, null=True)
    modal = models.CharField(max_length=100,blank=True, null=True)
    campo_livre_1 = models.CharField(max_length=100, blank=True, null=True)
    campo_livre_2 = models.CharField(max_length=100, blank=True, null=True)
    campo_livre_3 = models.CharField(max_length=100, blank=True, null=True)
    campo_livre_4 = models.CharField(max_length=100, blank=True, null=True)
    campo_livre_5 = models.CharField(max_length=100, blank=True, null=True)

    dados=models.JSONField(blank=True, null=True)

    @property
    def valor(self):
        return sum(n.valor for n in self.notas.all())

    @property
    def peso(self):
        return sum(n.peso for n in self.notas.all())
    
    def __str__(self):
        return f"Manifesto {self.numero_rota} - {self.rota_destino}"

# Modelo Parada
