from django.urls import path
from app_medic_search.views.ProfileViewer import list_profile_view, edit_profile


urlpatterns = [
    path('', list_profile_view, name='profiles'),
    path('<int:id>', list_profile_view, name='profile'),
    path('edit/', edit_profile, name='edit_profile'),
    
]