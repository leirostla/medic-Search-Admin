from django.urls import path
from app_medic_search.views.MedicoView import list_medico_view


urlpatterns = [
    path('', list_medico_view, name='medicos'),
]