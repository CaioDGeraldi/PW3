from unittest.mock import Mock, patch

import requests
from django.test import TestCase
from django.urls import reverse


class BuscarCepTests(TestCase):
    @patch("integracao.views.requests.get")
    def test_retorna_endereco(self, get):
        resposta = Mock()
        resposta.json.return_value = {
            "logradouro": "Praça da Sé",
            "bairro": "Sé",
            "localidade": "São Paulo",
            "uf": "SP",
        }
        get.return_value = resposta

        response = self.client.get(reverse("buscar_cep", args=["01001000"]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["endereco"], "Praça da Sé")
        self.assertEqual(response.json()["bairro"], "Sé")
        self.assertEqual(response.json()["cidade"], "São Paulo")
        self.assertEqual(response.json()["estado"], "SP")
        self.assertNotIn("ibge", response.json())
        get.assert_called_once_with(
            "https://viacep.com.br/ws/01001000/json/",
            timeout=5,
        )

    def test_rejeita_cep_invalido(self):
        response = self.client.get(reverse("buscar_cep", args=["1234"]))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"erro": "CEP inválido."})

    @patch("integracao.views.requests.get")
    def test_cep_nao_encontrado(self, get):
        resposta = Mock()
        resposta.json.return_value = {"erro": True}
        get.return_value = resposta

        response = self.client.get(reverse("buscar_cep", args=["00000000"]))

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"erro": "CEP não encontrado."})

    @patch("integracao.views.requests.get", side_effect=requests.Timeout)
    def test_falha_na_consulta_externa(self, get):
        response = self.client.get(reverse("buscar_cep", args=["01001000"]))

        self.assertEqual(response.status_code, 502)
        self.assertEqual(response.json(), {"erro": "Falha ao consultar a API externa."})

    @patch("integracao.views.requests.get")
    def test_resposta_externa_invalida(self, get):
        resposta = Mock()
        resposta.json.side_effect = ValueError
        get.return_value = resposta

        response = self.client.get(reverse("buscar_cep", args=["01001000"]))

        self.assertEqual(response.status_code, 502)
        self.assertEqual(response.json(), {"erro": "Resposta inválida da API externa."})
