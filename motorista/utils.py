import requests
from requests.exceptions import RequestException
from .models import Motorista

# Defina a URL da API e a chave de autenticação (key)
API_URL = "https://api.jsonbin.io/v3/b/680a9bdc8960c979a58c6aa2"
API_KEY = "$2a$10$j26vqK9KYZXKKyIONFMpo.Uh2prDadcMmhMzgeYEzBgxCtSiggepC"  # Substitua pela sua chave de autenticação

def registrar_motoristas():
    headers = {
        'X-Master-Key': API_KEY  # Chave de autenticação da API
    }

    # Tente obter todos os motoristas, mesmo que a resposta seja limitada (sem paginação)
    page = 1  # Inicia na primeira página

    while True:
        try:
            # Faz a requisição para a página atual
            response = requests.get(f"{API_URL}?page={page}", headers=headers)
            response.raise_for_status()  # Isso levanta uma exceção para códigos de status HTTP 4xx/5xx

            if response.status_code == 200:
                data = response.json()  # Recebe os dados no formato JSON
                motoristas_data = data.get('record', [])
                
                if not motoristas_data:
                    print("Nenhum motorista encontrado.")
                    break

                # Processa os motoristas retornados na página atual
                for motorista in motoristas_data:
                    cpf = motorista.get('owner_cpf')
                    nome = motorista.get('name')
                    cnh = motorista.get('cnh')
                    placa = motorista.get('plate', None)
                    mobile_person_id = motorista.get('mobile_person_id')

                    # Remover pontos e traços do CPF e CNH
                    cpf = cpf.replace(".", "").replace("-", "") if cpf else None
                    cnh = cnh.replace(".", "").replace("-", "") if cnh else None

                    # Verificar se o motorista já está registrado
                    motorista_existente = Motorista.objects.filter(cpf=cpf).first()

                    if motorista_existente:
                        print(f"Motorista {nome} já está registrado.")
                    else:
                        # Se o motorista não existir, criar e registrar no banco de dados
                        motorista_db = Motorista.objects.create(
                            cpf=cpf,
                            nome=nome,
                            cnh=cnh,
                            placa=placa,
                            mobile_person_id=mobile_person_id
                        )
                        print(f"Motorista {nome} registrado com sucesso!")

                # Se a resposta não contiver a chave 'next_page', significa que não há mais páginas.
                # Vamos então parar de buscar novas páginas.
                if 'next_page' not in data or not data['next_page']:
                    print("Todos os motoristas foram processados.")
                    break
                else:
                    page += 1  # Se houver uma próxima página, incrementa o número da página

            else:
                print(f"Erro ao acessar a API: {response.status_code}")
                break

        except RequestException as e:
            print(f"Erro na requisição: {e}")
            break