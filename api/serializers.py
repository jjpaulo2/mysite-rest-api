from rest_framework.serializers import ModelSerializer
from api.models import ( Sobre, 
                         ParagrafoDescricao, 
                         RedeSocial, 
                         Experiencia, 
                         Educacao, 
                         ProjetoEducacao, 
                         Habilidade,
                         Portfolio )

class SobreSerializer(ModelSerializer):
    class Meta:
        model = Sobre
        fields = ['nome', 'sobrenome', 'cidade', 'telefone', 'lattes']

class ParagrafoDescricaoSerializer(ModelSerializer):
    class Meta:
        model = ParagrafoDescricao
        fields = ['paragrafo']

class RedeSocialSerializer(ModelSerializer):
    class Meta:
        model = RedeSocial
        fields = ['nome', 'icone', 'link']

class ExperienciaSerializer(ModelSerializer):
    class Meta:
        model = Experiencia
        fields = ['empresa', 'cargo', 'inicio', 'fim', 'descricao']

class EducacaoSerializer(ModelSerializer):
    class Meta:
        model = Educacao
        fields = ['instituicao', 'titulo', 'inicio', 'fim']

class ProjetoEducacaoSerializer(ModelSerializer):
    class Meta:
        model = ProjetoEducacao
        fields = ['instituicao', 'titulo', 'ano', 'descricao']

class HabilidadeSerializer(ModelSerializer):
    class Meta:
        model = Habilidade
        fields = ['titulo', 'icone', 'descricao']

class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['titulo', 'descricao', 'gif']