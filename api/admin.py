from django.contrib import admin
from api.models import ( Sobre, 
                         ParagrafoDescricao, 
                         RedeSocial, 
                         Experiencia, 
                         Educacao, 
                         ProjetoEducacao, 
                         Habilidade )

# Register your models here.
admin.site.register(Sobre)
admin.site.register(ParagrafoDescricao)
admin.site.register(RedeSocial)
admin.site.register(Experiencia)
admin.site.register(Educacao)
admin.site.register(ProjetoEducacao)
admin.site.register(Habilidade)