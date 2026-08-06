from django.contrib import admin

from app_medic_search.models.bairros import Bairros
from app_medic_search.models.cidade import Cidade
from app_medic_search.models.endereco import Endereco
from app_medic_search.models.especialidade import Especialidade
from app_medic_search.models.estado import Estado
from app_medic_search.models.profile import Profile
from app_medic_search.models.rating import Rating
from app_medic_search.models.dia_da_semana import Dia_Semana


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'especialidadesList', 'enderecosList',)
    
    def especialidadesList(self, obj):
        return ", ".join([e.name for e in obj.especialidades.all()])

    def enderecosList(self, obj):
        return ", ".join([addr.address for addr in obj.enderecos.all()])

    # list_filter = ('user__is_active',)
    # list_display = ('user', 'role', 'birthday')
    # list_display_links = ('user','role')
    # empty_value_display = 'Vazio'
    #date_hierarchy = 'created_at'


# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Bairros)
admin.site.register(Cidade)
admin.site.register(Dia_Semana)
admin.site.register(Endereco)
admin.site.register(Especialidade)
admin.site.register(Estado)
admin.site.register(Rating)