import requests
from motorista.models import Motorista
from .models import Manifesto, Transportadora, Endereco
from django.utils.dateparse import parse_datetime
from datetime import datetime

def criar_manifesto():
    # 1. Busca o JSON
    url = "https://api.jsonbin.io/v3/b/680ba6678960c979a58cfdb6"
    headers = {"X-Master-Key": "$2a$10$j26vqK9KYZXKKyIONFMpo.Uh2prDadcMmhMzgeYEzBgxCtSiggepC"}
    response = requests.get(url, headers=headers)
    data = response.json()['record']  # Pega o dicionário "Manifesto"

    manifesto_data = data["Manifesto"]
    motorista_data = manifesto_data["Motorista"]

    # 2. Verifica se motorista existe
    cpf = motorista_data["CPF"]
    motorista = Motorista.objects.filter(cpf=cpf).first()

    if not motorista:
        motorista = Motorista.objects.create(
            nome=motorista_data["Nome"],
            cpf=cpf,
            cnh=motorista_data["CNH"],
            placa=motorista_data["PlacaCaminhao"]           
        )
        print(f"Motorista criado: {motorista}")

    # 3. Cria ou recupera a transportadora
    transportadora_nome = manifesto_data["Transportadora"]
    transportadora, _ = Transportadora.objects.get_or_create(
        razao=transportadora_nome,
        defaults={'codigo': 'AUTOMATICO'}        
    )

    # Recupera ou cria o manifesto
    manifesto, created = Manifesto.objects.get_or_create(
        motorista=motorista,
        numero_rota=manifesto_data["ID"],
        data=manifesto_data["DataEmissao"],
        transportadora=transportadora,
        origem=manifesto_data["Origem"],
        destino=manifesto_data["Destino"],
        
    )
    # Agora, cria os dados que vão ser armazenados no JSONField
    dados = []

    # Itera sobre as Notas do manifesto
    for nota_data in manifesto_data["Notas"]:
        dados.append({
            "numero": nota_data["Numero"],
            "destinatario": nota_data["RazaoSocial"],
            "endereco_entrega": nota_data["EnderecoEntrega"],
            "documento_numero": nota_data["CNPJDestinatario"],
            "produtos": nota_data["Produtos"]
        })

    # Agora, armazena os dados no manifesto
    manifesto.dados = dados
    manifesto.save()

    if not created:
        # Atualiza os campos se já existia
        manifesto.status = manifesto_data.get("Status", manifesto.status)
        manifesto.rota_destino = manifesto_data.get("RotaDestino", manifesto.rota_destino)
        manifesto.rota_nome = manifesto_data.get("RotaNome", manifesto.rota_nome)
        manifesto.limites_inicio = manifesto_data.get("LimiteInicio", manifesto.limites_inicio)
        manifesto.limites_fim = manifesto_data.get("LimiteFim", manifesto.limites_fim)
        manifesto.tipo_rota = manifesto_data.get("TipoRota", manifesto.tipo_rota)
        manifesto.tipo_material = manifesto_data.get("TipoMaterial", manifesto.tipo_material)
        manifesto.fornecimento = manifesto_data.get("Fornecimento", manifesto.fornecimento)
        manifesto.tipo_frete = manifesto_data.get("TipoFrete", manifesto.tipo_frete)
        manifesto.modal = manifesto_data.get("Modal", manifesto.modal)
        manifesto.campo_livre_1 = manifesto_data.get("CampoLivre1", manifesto.campo_livre_1)
        manifesto.campo_livre_2 = manifesto_data.get("CampoLivre2", manifesto.campo_livre_2)
        manifesto.campo_livre_3 = manifesto_data.get("CampoLivre3", manifesto.campo_livre_3)
        manifesto.campo_livre_4 = manifesto_data.get("CampoLivre4", manifesto.campo_livre_4)
        manifesto.campo_livre_5 = manifesto_data.get("CampoLivre5", manifesto.campo_livre_5)
        manifesto.save()

    print(f"{'Criado' if created else 'Atualizado'} manifesto: {manifesto}")
    
    return motorista , transportadora, manifesto