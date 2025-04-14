import requests

def iniciar_transporte_api(manifesto_id):
    url = "https://subdominio.eslcloud.com.br/graphql"
    query = """mutation manifestStartTransport($id: ID!, $params: ManifestStartTransportInput!){
        manifestStartTransport(id: $id, params: $params){
            errors
            success
            resource {
                id
                departuredAt
            }
        }
    }"""
    variables = {
        "id": str(manifesto_id),
        "params": {
            "departuredAt": "2025-04-10T10:00:00Z"
        }
    }
    payload = {"query": query, "variables": variables}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    print("Início transporte:", response.text)

def finalizar_transporte_api(manifesto_id):
    url = "https://subdominio.eslcloud.com.br/graphql"
    query = """mutation manifestClose($id: ID, $sequenceCode: String, $params: ManifestCloseInput!){
        manifestClose(id: $id, sequenceCode: $sequenceCode, params: $params){
            errors
            success
            resource {
                id
                closedAt
            }
        }
    }"""
    variables = {
        "id": str(manifesto_id),
        "params": {
            "closedAt": "2025-04-10T16:00:00Z"
        }
    }
    payload = {"query": query, "variables": variables}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    print("Fechamento:", response.text)
