from django.urls import path
from app_medic_search.views.AuthView import login_view

urlpatterns = [
    path('login/', login_view, name='login'),
]