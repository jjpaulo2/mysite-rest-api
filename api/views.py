from rest_framework.viewsets import ReadOnlyModelViewSet
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

class SobreViewSet(ReadOnlyModelViewSet):
    queryset = Sobre.objects.all()
    serializer_class = SobreSerializer

class ParagrafoDescricaoViewSet(ReadOnlyModelViewSet):
    queryset = ParagrafoDescricao.objects.all()
    serializer_class = ParagrafoDescricaoSerializer

class RedeSocialViewSet(ReadOnlyModelViewSet):
    queryset = RedeSocial.objects.all()
    serializer_class = RedeSocialSerializer

class ExperienciaViewSet(ReadOnlyModelViewSet):
    queryset = Experiencia.objects.all()
    serializer_class = ExperienciaSerializer

class EducacaoViewSet(ReadOnlyModelViewSet):
    queryset = Educacao.objects.all()
    serializer_class = EducacaoSerializer

class ProjetoEducacaoViewSet(ReadOnlyModelViewSet):
    queryset = ProjetoEducacao.objects.all()
    serializer_class = ProjetoEducacaoSerializer

class HabilidadeViewSet(ReadOnlyModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer