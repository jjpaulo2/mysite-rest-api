from rest_framework import viewsets
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

class SobreViewSet(viewsets.ModelViewSet):
    queryset = Sobre.objects.all()
    serializer_class = SobreSerializer

class ParagrafoDescricaoViewSet(viewsets.ModelViewSet):
    queryset = ParagrafoDescricao.objects.all()
    serializer_class = ParagrafoDescricaoSerializer

class RedeSocialViewSet(viewsets.ModelViewSet):
    queryset = RedeSocial.objects.all()
    serializer_class = RedeSocialSerializer

class ExperienciaViewSet(viewsets.ModelViewSet):
    queryset = Experiencia.objects.all()
    serializer_class = ExperienciaSerializer

class EducacaoViewSet(viewsets.ModelViewSet):
    queryset = Educacao.objects.all()
    serializer_class = EducacaoSerializer

class ProjetoEducacaoViewSet(viewsets.ModelViewSet):
    queryset = ProjetoEducacao.objects.all()
    serializer_class = ProjetoEducacaoSerializer

class HabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer