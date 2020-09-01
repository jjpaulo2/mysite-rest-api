from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token

def generic_setup(self: any, is_authenticated: bool):
    self.client = APIClient()

    if is_authenticated:
        self.test_user = User.objects.create( username='test_user',
                                                password='123',
                                                is_superuser=True,
                                                email='teste@teste.com' )
        self.token = Token.objects.create(user=self.test_user)
        self.request_header = {
            'HTTP_AUTHORIZATION': 'Token ' + self.token.key
        }

class TestAuthenticatedAllowedMethods(APITestCase):

    def setUp(self):
        generic_setup(self, True)

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


class TestAuthenticatedDenyMethods(APITestCase):

    def setUp(self):
        generic_setup(self, True)

    def test_post_sobre(self):
        url = '/sobre/'
        response = self.client.post(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_sobre(self):
        url = '/sobre/'
        response = self.client.put(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_sobre(self):
        url = '/sobre/'
        response = self.client.delete(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_paragrafos_descricao(self):
        url = '/paragrafos-descricao/'
        response = self.client.post(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_paragrafos_descricao(self):
        url = '/paragrafos-descricao/'
        response = self.client.put(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_paragrafos_descricao(self):
        url = '/paragrafos-descricao/'
        response = self.client.delete(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_redes_sociais(self):
        url = '/redes-sociais/'
        response = self.client.post(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_redes_sociais(self):
        url = '/redes-sociais/'
        response = self.client.put(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_redes_sociais(self):
        url = '/redes-sociais/'
        response = self.client.delete(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_experiencia(self):
        url = '/experiencia/'
        response = self.client.post(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_experiencia(self):
        url = '/experiencia/'
        response = self.client.put(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_experiencia(self):
        url = '/experiencia/'
        response = self.client.delete(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_educacao(self):
        url = '/educacao/'
        response = self.client.post(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_educacao(self):
        url = '/educacao/'
        response = self.client.put(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_educacao(self):
        url = '/educacao/'
        response = self.client.delete(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_projetos_educacao(self):
        url = '/projetos-educacao/'
        response = self.client.post(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_projetos_educacao(self):
        url = '/projetos-educacao/'
        response = self.client.put(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_projetos_educacao(self):
        url = '/projetos-educacao/'
        response = self.client.delete(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_habilidades(self):
        url = '/habilidades/'
        response = self.client.post(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_habilidades(self):
        url = '/habilidades/'
        response = self.client.put(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_habilidades(self):
        url = '/habilidades/'
        response = self.client.delete(url, **self.request_header)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

class TestNonAuthenticatedAllMethods(APITestCase):

    def setUp(self):
        generic_setup(self, False)

    def test_get_sobre(self):
        url = '/sobre/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_sobre(self):
        url = '/sobre/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_sobre(self):
        url = '/sobre/'
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_sobre(self):
        url = '/sobre/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_paragrafos_descricao(self):
        url = '/paragrafos-descricao/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_paragrafos_descricao(self):
        url = '/paragrafos-descricao/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_paragrafos_descricao(self):
        url = '/paragrafos-descricao/'
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_paragrafos_descricao(self):
        url = '/paragrafos-descricao/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_redes_sociais(self):
        url = '/redes-sociais/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_redes_sociais(self):
        url = '/redes-sociais/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_redes_sociais(self):
        url = '/redes-sociais/'
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_redes_sociais(self):
        url = '/redes-sociais/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_experiencia(self):
        url = '/experiencia/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_experiencia(self):
        url = '/experiencia/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_experiencia(self):
        url = '/experiencia/'
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_experiencia(self):
        url = '/experiencia/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_educacao(self):
        url = '/educacao/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_educacao(self):
        url = '/educacao/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_educacao(self):
        url = '/educacao/'
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_educacao(self):
        url = '/educacao/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_projetos_educacao(self):
        url = '/projetos-educacao/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_projetos_educacao(self):
        url = '/projetos-educacao/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_projetos_educacao(self):
        url = '/projetos-educacao/'
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_projetos_educacao(self):
        url = '/projetos-educacao/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_habilidades(self):
        url = '/habilidades/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_habilidades(self):
        url = '/habilidades/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_habilidades(self):
        url = '/habilidades/'
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_habilidades(self):
        url = '/habilidades/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)