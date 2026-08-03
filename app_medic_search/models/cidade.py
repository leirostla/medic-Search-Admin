from app_medic_search.models import *
from app_medic_search.models.estado import Estado

class Cidade(models.Model):
    state = models.ForeignKey(Estado, null=True, related_name='state', on_delete=models.SET_NULL)
    name = models.CharField(null=False, max_length=20)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.state.name)