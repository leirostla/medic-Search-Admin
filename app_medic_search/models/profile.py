
from app_medic_search.models import *
from app_medic_search.models.especialidade import Especialidade
from app_medic_search.models.endereco import Endereco

# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICE, default=3)
    birthday = models.DateField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    favoritos = models.ManyToManyField(User, blank=True, related_name='favoritos')
    especialidades = models.ManyToManyField(Especialidade, blank=True, related_name='especialidades')
    enderecos = models.ManyToManyField(Endereco, blank=True, related_name='enderecos')

    def __str__(self):
        return '{}'.format(self.user.username)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass