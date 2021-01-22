from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.models import ( Sobre, 
                         ParagrafoDescricao, 
                         RedeSocial, 
                         Experiencia, 
                         Educacao, 
                         ProjetoEducacao, 
                         Habilidade,
                         Portfolio )
from api.serializers import ( SobreSerializer,
                              ParagrafoDescricaoSerializer,
                              RedeSocialSerializer,
                              ExperienciaSerializer,
                              EducacaoSerializer,
                              ProjetoEducacaoSerializer,
                              HabilidadeSerializer,
                              PortfolioSerializer )

# Create your views here.

class SobreViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Sobre.objects.all()
    serializer_class = SobreSerializer

class ParagrafoDescricaoViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = ParagrafoDescricao.objects.all().order_by('id')
    serializer_class = ParagrafoDescricaoSerializer

class RedeSocialViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = RedeSocial.objects.all()
    serializer_class = RedeSocialSerializer

class ExperienciaViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Experiencia.objects.all()
    serializer_class = ExperienciaSerializer

class EducacaoViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Educacao.objects.all()
    serializer_class = EducacaoSerializer

class ProjetoEducacaoViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = ProjetoEducacao.objects.all()
        instituicao = self.request.query_params.get('instituicao', None)
        if instituicao is not None:
            queryset = queryset.filter(instituicao=instituicao)
        
        return queryset

    serializer_class = ProjetoEducacaoSerializer

class HabilidadeViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer

class PortfolioViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer