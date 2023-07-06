from django.contrib import admin
from. models import *
# Register your models here.

# imagens para banner principal da pagina
class BannerAdminIndex(admin.ModelAdmin):
    list_display = ('imagem',)
admin.site.register(Banner,BannerAdminIndex)

# icons e links contactos para tabs ligar 
class ContactosAdmin(admin.ModelAdmin):
    list_display = ('icon','contacto','titulo')


admin.site.register(Contactos,ContactosAdmin)

class SigaAdmin(admin.ModelAdmin):
    list_display = ('icon','titulo','link')

admin.site.register(Siga,SigaAdmin)

# imagens para servicos pagina principal
class DemoServicosAdmin(admin.ModelAdmin):
    list_display = ('imagem','titulo','titulo_link','link')
admin.site.register(DemoServicos,DemoServicosAdmin)

#imagens e titulo para pagina fotos
class FotosAllAdminindex(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Fotos_all,FotosAllAdminindex)

#imagens e titulo para pagina fotos exterior
class FotosExteriorAdminindex(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Fotos_exterior_home,FotosExteriorAdminindex)

#imagens e titulo para pagina fotos quartos
class FotosQuartosAdminindex(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Fotos_quartos_home,FotosQuartosAdminindex)

#imagens e titulo para pagina fotos
class FotosRestauranteAdminindex(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Fotos_restaurante_home,FotosRestauranteAdminindex)


# pagina restaurante
class BannerAdminRestaurante(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Banner_restaurante,BannerAdminRestaurante)

class FotosAllAdminres(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Fotos_all_restaurante,FotosAllAdminres)

class FotosRestauranteAdmin(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Fotos_restaurante,FotosRestauranteAdmin)
class FotosOutrasAdminRestaurante(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Fotos_outras_restaurante,FotosOutrasAdminRestaurante)


# pagina auditorio
class BannerAdminAuditorio(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Banner_auditorio,BannerAdminAuditorio)

class FotosAllAdminAuditorio(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Fotos_all_auditorio,FotosAllAdminAuditorio)

# pagina quartos
class BannerAdminQuartos(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Banner_quartos,BannerAdminQuartos)


class FotosAllAdminQuartos(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Fotos_all_quartos,FotosAllAdminQuartos)
class FotosQuartosAdmin(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Fotos_quartos,FotosQuartosAdmin)
class FotosOutrasAdminQuartos(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Fotos_outras_quartos,FotosOutrasAdminQuartos)
class PrecoQuartosAdmin(admin.ModelAdmin):
    list_display = ('imagem','titulo','status','preco')
    list_editable = ('titulo','status','preco')
admin.site.register(Quartos_preco,PrecoQuartosAdmin)

# pagina piscina
class BannerAdminPiscina(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Banner_piscina,BannerAdminPiscina)

class FotosAllAdminPiscina(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Fotos_all_piscina,FotosAllAdminPiscina)

# pagina Jardim para eventos ao ar livre
class BannerAdminJardim(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Banner_jardim,BannerAdminJardim)

class FotosAllAdminJardim(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Fotos_all_jardim,FotosAllAdminJardim)

# pagina jardim infantil
class BannerAdminJardimInfantil(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Banner_jardim_infantil,BannerAdminJardimInfantil)

class FotosAllAdminJardimInfantil(admin.ModelAdmin):
    list_display = ('imagem','titulo')
admin.site.register(Fotos_all_jardim_infantil,FotosAllAdminJardimInfantil)

class Localizacao_mapaAdmin(admin.ModelAdmin):
    list_display = ('localizacao',)
    
admin.site.register(Localizacao_mapa,Localizacao_mapaAdmin)
