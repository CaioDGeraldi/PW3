import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def buscar_cep(request, cep):
    if len(cep) != 8 or not cep.isdigit():
        return Response({"erro": "CEP inválido."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()
    except requests.RequestException:
        return Response(
            {"erro": "Falha ao consultar a API externa."},
            status=status.HTTP_502_BAD_GATEWAY,
        )
    except ValueError:
        return Response(
            {"erro": "Resposta inválida da API externa."},
            status=status.HTTP_502_BAD_GATEWAY,
        )

    if dados.get("erro"):
        return Response({"erro": "CEP não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    return Response({
        "mensagem": "Dados consumidos com sucesso pela nossa API!",
        "endereco": dados.get("logradouro", ""),
        "bairro": dados.get("bairro", ""),
        "cidade": dados.get("localidade", ""),
        "estado": dados.get("uf", ""),
    })
