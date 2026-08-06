from django.urls import path
from app_medic_search.views.ProfileViewer import list_profile_view

urlpatterns = [
    path('<int:id>', list_profile_view, name='profile'),
    path('', list_profile_view, name='profiles'),
]