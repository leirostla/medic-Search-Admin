from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Médico'),
    (3, 'Paciente')
)

from .profile import Profile
from .bairros import Bairros
from .cidade import Cidade
from .dia_da_semana import Dia_Semana
from .endereco import Endereco
from .especialidade import Especialidade
from .estado import Estado
from .rating import Rating
