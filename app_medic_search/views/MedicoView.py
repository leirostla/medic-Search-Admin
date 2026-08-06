from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator

from app_medic_search.models.profile import Profile

def list_medico_view(request):

    nome = request.GET.get('nome')
    especialidade = request.GET.get('especialidade')
    bairro = request.GET.get('bairro')
    cidade = request.GET.get('cidade')
    estado = request.GET.get('estado')

    medicos = Profile.objects
    if nome is not None and nome != '':
        print('Nome: %s' % nome)
        medicos = medicos.filter(Q(user__username__contains=nome) | Q(user__first_name__contains=nome))
    if especialidade is not None:
        print('Especialidade: %s' % especialidade)
        medicos = medicos.filter(especialidades__id=especialidade)
    if bairro is not None:
        print('Bairro: %s' % bairro)
        medicos = medicos.filter(enderecos__neighborhood=bairro)
    elif cidade is not None:
        print('Cidade: %s' % cidade)
        medicos = medicos.filter(enderecos__neighborhood__city=cidade)
    elif estado is not None:
        print('Estado: %s' % estado)
        medicos = medicos.filter(enderecos__neighborhood__city__state=estado)

    if len(medicos) > 0:
        paginator = Paginator(medicos, 8)
        page = request.GET.get('page')
        medicos = paginator.get_page(page)

    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()

    context = {
        'medicos': medicos,
        'parameters': parameters
    }
   
    return render(request, template_name='medicos/list.html', context=context, status=200)
