import requests
from .models import Motorista

def importar_motoristas_da_api():
    url = 'https://api.empresa.com.br/motoristas'  # exemplo
    response = requests.get(url)
    
    if response.status_code == 200:
        motoristas = response.json()
        for m in motoristas:
            Motorista.objects.update_or_create(
                cpf=m['cpf'],
                defaults={
                    'nome': m['nome'],
                    'cnh': m['cnh'],
                    'placa': m['placa']
                }
            )