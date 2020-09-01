from rest_framework import serializers
from api.models import ( Sobre, 
                         ParagrafoDescricao, 
                         RedeSocial, 
                         Experiencia, 
                         Educacao, 
                         ProjetoEducacao, 
                         Habilidade )

class SobreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobre
        fields = ['nome', 'sobrenome', 'cidade', 'telefone', 'lattes']

class ParagrafoDescricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParagrafoDescricao
        fields = ['paragrafo']

class RedeSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedeSocial
        fields = ['nome', 'icone', 'link']

class ExperienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiencia
        fields = ['empresa', 'cargo', 'inicio', 'fim', 'descricao']

class EducacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educacao
        fields = ['instituicao', 'titulo', 'inicio', 'fim', 'descricao']

class ProjetoEducacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjetoEducacao
        fields = ['instituicao', 'titulo', 'ano', 'descricao']

class HabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidade
        fields = ['titulo', 'icone', 'nivel']