# Consulta de CEP

API intermediária desenvolvida com Django REST Framework. Recebe um CEP, consulta a API do ViaCEP e retorna os dados de endereço selecionados.

## Executar localmente

No CMD, na pasta do projeto:

```cmd
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py runserver
```

Antes de executar, substitua o valor de `DJANGO_SECRET_KEY` no arquivo `.env` por uma chave local.

## Endpoint

```http
GET /api/consulta-cep/01001000/
```

A resposta contém a mensagem de sucesso, logradouro, bairro, cidade e estado.
