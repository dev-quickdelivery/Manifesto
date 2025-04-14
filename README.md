# 📦 ManifestoJa

**ManifestoJa** é um sistema web para gerenciamento de transportes, desenvolvido com Django e integrado à API da ESL Cloud para iniciar e encerrar manifestos de forma prática e automatizada.

---

## 🚛 Funcionalidades Principais

- Cadastro e gerenciamento de **motoristas**
- Criação e controle de **manifestos de transporte**
- Registro de **notas fiscais** associadas aos manifestos
- Upload e controle de **canhotos (comprovantes de entrega)**
- Integração com API GraphQL da ESL Cloud para:
  - ✅ Iniciar transporte
  - 🛑 Encerrar transporte
- Interface administrativa amigável (Django Admin)
- Log de ações diretamente no painel com feedback da API

---

## 🔧 Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Django 4+](https://www.djangoproject.com/)
- [Requests](https://docs.python-requests.org/)
- HTML5, CSS3 (via Django Admin)
- API GraphQL da ESL Cloud

---

## 📂 Estrutura do Projeto

```
manifestoja/
├── app/
│   ├── models.py           # Modelos: Motorista, Manifesto, Nota, Canhoto
│   ├── views.py            # Lógica para iniciar/finalizar manifestos
│   ├── admin.py            # Interface personalizada no Django Admin
│   ├── utils.py            # Integração com API GraphQL
│   └── ...
├── manage.py
├── README.md
└── requirements.txt
```

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/manifestoja.git
cd manifestoja
```

### 2. Crie o ambiente virtual e ative

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute as migrações

```bash
python manage.py migrate
```

### 5. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 6. Inicie o servidor

```bash
python manage.py runserver
```

Acesse o painel de administração em: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 🔌 Integração com a API ESL Cloud (GraphQL)

O sistema se comunica com a API da ESL Cloud usando **mutations GraphQL** para iniciar e encerrar manifestos.

- 📤 **Início de transporte**:
  - Mutation: `manifestStartTransport`
  - Enviada ao clicar em **“Iniciar”** no Django Admin

- 📥 **Fechamento do manifesto**:
  - Mutation: `manifestClose`
  - Enviada ao clicar em **“Finalizar”**

Essas operações são feitas automaticamente pelas funções no arquivo `utils.py`, que utilizam `requests` para enviar as queries.

---

## ✍️ Exemplo de uso

1. Acesse o painel `/admin`
2. Crie um motorista
3. Crie um manifesto e associe o motorista
4. Adicione notas fiscais ao manifesto
5. Clique em **Iniciar** ou **Finalizar** no painel para testar a API

---

## 🛠️ Futuras Melhorias

- Upload de canhotos via formulário
- Dashboard de KPIs (ex: total de notas por período)
- Notificações por e-mail/SMS
- Filtros avançados por status, motorista ou data

---

## 🤝 Contribuição

Sinta-se livre para abrir *issues*, enviar *pull requests* ou sugerir melhorias! Este projeto é aberto para aprendizado e evolução.

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📬 Contato

Desenvolvido por [Seu Nome](https://github.com/lgluiz1)

