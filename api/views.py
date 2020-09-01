from rest_framework.viewsets import ModelViewSet
from api.models import ( Sobre, 
                         ParagrafoDescricao, 
                         RedeSocial, 
                         Experiencia, 
                         Educacao, 
                         ProjetoEducacao, 
                         Habilidade )
from api.serializers import ( SobreSerializer,
                              ParagrafoDescricaoSerializer,
                              RedeSocialSerializer,
                              ExperienciaSerializer,
                              EducacaoSerializer,
                              ProjetoEducacaoSerializer,
                              HabilidadeSerializer )

# Create your views here.

class SobreViewSet(ModelViewSet):
    queryset = Sobre.objects.all()
    serializer_class = SobreSerializer

class ParagrafoDescricaoViewSet(ModelViewSet):
    queryset = ParagrafoDescricao.objects.all()
    serializer_class = ParagrafoDescricaoSerializer

class RedeSocialViewSet(ModelViewSet):
    queryset = RedeSocial.objects.all()
    serializer_class = RedeSocialSerializer

class ExperienciaViewSet(ModelViewSet):
    queryset = Experiencia.objects.all()
    serializer_class = ExperienciaSerializer

class EducacaoViewSet(ModelViewSet):
    queryset = Educacao.objects.all()
    serializer_class = EducacaoSerializer

class ProjetoEducacaoViewSet(ModelViewSet):
    queryset = ProjetoEducacao.objects.all()
    serializer_class = ProjetoEducacaoSerializer

class HabilidadeViewSet(ModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer