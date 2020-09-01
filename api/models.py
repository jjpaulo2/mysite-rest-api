from django.db import models

class Sobre(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    lattes = models.CharField(max_length=255)

class ParagrafoDescricao(models.Model):
    paragrafo = models.TextField(max_length=1000)

class RedeSocial(models.Model):
    nome = models.CharField(max_length=50)
    icone = models.CharField(max_length=20, verbose_name='Classe de ícone do FontAwesome')
    link = models.CharField(max_length=200)

class Experiencia(models.Model):
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    inicio = models.CharField(max_length=50)
    fim = models.CharField(max_length=50)
    descricao = models.TextField(max_length=1000)

class Educacao(models.Model):
    instituicao = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    inicio = models.CharField(max_length=50)
    fim = models.CharField(max_length=50)

class ProjetoEducacao(models.Model):
    instituicao = models.OneToOneField(Educacao, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField()
    descricao = models.CharField(max_length=500)

class Habilidade(models.Model):
    titulo = models.CharField(max_length=50)
    icone = models.CharField(max_length=20, verbose_name='Classe de ícone do DevIcon')
    nivel = models.IntegerField()
