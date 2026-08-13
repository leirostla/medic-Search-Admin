from django.urls import path
from app_medic_search.views.MedicoView import add_favorito_view, list_medico_view, remove_favorite_view


urlpatterns = [
        path('', list_medico_view, name='medicos'),
        path('favorito/', add_favorito_view, name='medico_favorito'),
        path('favorito/remover/', remove_favorite_view, name='medico_remover_favorito'),

]