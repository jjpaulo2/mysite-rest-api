from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token

class TestMySiteAPI(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.test_user = User.objects.create( username='test_user',
                                              password='123',
                                              is_superuser=True,
                                              email='teste@teste.com' )
        self.token = Token.objects.create(user=self.test_user)
        self.request_header = {
            'HTTP_AUTHORIZATION': 'Token ' + self.token.key
        }

    def test_get_sobre(self):
        url = '/sobre/'
        response = self.client.get(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_paragrafos_descricao(self):
        url = '/paragrafos-descricao/'
        response = self.client.get(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_redes_sociais(self):
        url = '/redes-sociais/'
        response = self.client.get(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_experiencia(self):
        url = '/experiencia/'
        response = self.client.get(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_educacao(self):
        url = '/educacao/'
        response = self.client.get(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_projetos_educacao(self):
        url = '/projetos-educacao/'
        response = self.client.get(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_habilidades(self):
        url = '/habilidades/'
        response = self.client.get(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)