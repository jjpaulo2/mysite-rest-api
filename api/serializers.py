from rest_framework.serializers import ModelSerializer, SerializerMethodField, PrimaryKeyRelatedField
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
        fields = ['nome', 'sobrenome', 'cidade', 'telefone', 'lattes', 'foto']

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

class ProjetoEducacaoSerializer(ModelSerializer):
    class Meta:
        model = ProjetoEducacao
        fields = ['titulo', 'ano', 'descricao']

class EducacaoSerializer(ModelSerializer):
    projetos = ProjetoEducacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Educacao
        fields = ['instituicao', 'titulo', 'inicio', 'fim', 'projetos']

class HabilidadeSerializer(ModelSerializer):
    class Meta:
        model = Habilidade
        fields = ['titulo', 'icone', 'descricao']

class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['titulo', 'descricao', 'gif']