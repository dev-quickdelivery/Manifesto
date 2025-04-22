from django.db import models
from motorista.models import Motorista

class Manifesto(models.Model):
    STATUS_CHOICES = [
        ('Aguardando_Motorista', 'Aguardando'),
        ('Em_transporte', 'Em Transporte'),
        ('Finalizado', 'Finalizado'),
    ]
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Aguardando_Motorista')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    finalizado_em = models.DateTimeField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    @property
    def valor(self):
        return sum(n.valor for n in self.notas.all())

    @property
    def peso(self):
        return sum(n.peso for n in self.notas.all())

    def __str__(self):
        return f"Manifesto #{self.id} - {self.status}"

class Nota(models.Model):
    manifesto = models.ForeignKey(Manifesto, on_delete=models.CASCADE, related_name="notas")
    numero = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    peso = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Nota {self.numero}"

class Canhoto(models.Model):
    nota = models.OneToOneField(Nota, on_delete=models.CASCADE)
    recebido_em = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='canhotos/', blank=True, null=True)

    def __str__(self):
        return f"Canhoto da Nota {self.nota.numero}"
