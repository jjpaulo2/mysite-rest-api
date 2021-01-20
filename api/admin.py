from django.contrib import admin
from django.utils.safestring import mark_safe
from api.models import ( Sobre, 
                         ParagrafoDescricao, 
                         RedeSocial, 
                         Experiencia, 
                         Educacao, 
                         ProjetoEducacao, 
                         Habilidade,
                         Portfolio )

class MyAPIAdminSite(admin.AdminSite):
    site_header = 'Administração do site'
    site_title = 'Administração do site'
    index_title = 'João Paulo Carvalho'

admin.site = MyAPIAdminSite()

admin.site.register(ParagrafoDescricao)
admin.site.register(RedeSocial)
admin.site.register(Experiencia)
admin.site.register(Educacao)
admin.site.register(ProjetoEducacao)
admin.site.register(Habilidade)

@admin.register(Sobre, site=admin.site)
class SobreAdmin(admin.ModelAdmin):
    readonly_fields = ('previa_da_foto',)

    def previa_da_foto(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%;"/>'.format(
                url = obj.foto.url
            )
        )

@admin.register(Portfolio, site=admin.site)
class PortfolioAdmin(admin.ModelAdmin):
    readonly_fields = ('previa_da_foto',)

    def previa_da_foto(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%;"/>'.format(
                url = obj.gif.url
            )
        )