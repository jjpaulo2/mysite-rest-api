from rest_framework.routers import DefaultRouter
from api.views import ( SobreViewSet, 
                        ParagrafoDescricaoViewSet, 
                        RedeSocialViewSet, 
                        ExperienciaViewSet, 
                        EducacaoViewSet, 
                        ProjetoEducacaoViewSet, 
                        HabilidadeViewSet )

router = DefaultRouter()
router.register('sobre', SobreViewSet, basename='sobre')
router.register('paragrafos-descricao', ParagrafoDescricaoViewSet, basename='paragrafos-descricao')
router.register('redes-sociais', RedeSocialViewSet, basename='redes-sociais')
router.register('experiencia', ExperienciaViewSet, basename='experiencia')
router.register('educacao', EducacaoViewSet, basename='educacao')
router.register('projetos-educacao', ProjetoEducacaoViewSet, basename='projetos-educacao')
router.register('habilidades', HabilidadeViewSet, basename='habilidades')
