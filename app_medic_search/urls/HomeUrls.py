from django.urls import path
from app_medic_search.views.HomeView import home_view

urlpatterns = [
    path('', home_view, name='home'),
]