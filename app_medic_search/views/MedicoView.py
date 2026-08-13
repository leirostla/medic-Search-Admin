from django.db.models import Q
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from app_medic_search.models.profile import Profile

def list_medico_view(request):

    nome = request.GET.get('nome')
    especialidade = request.GET.get('especialidade')
    bairro = request.GET.get('bairro')
    cidade = request.GET.get('cidade')
    estado = request.GET.get('estado')

    medicos = Profile.objects.all()
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

    if medicos.exists():
        paginator = Paginator(medicos, 8)
        page = request.GET.get('page')
        medicos = paginator.get_page(page)

    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()

    context = {
        'medicos': medicos,
        'parameters': parameters
    }
   
    return render(request, template_name='medicos/medicos.html', context=context, status=200)

def add_favorito_view(request):
    page = request.POST.get("page")
    name = request.POST.get("name")
    speciality = request.POST.get("speciality")
    neighborhood = request.POST.get("neighborhood")
    city = request.POST.get("city")
    state = request.POST.get("state")
    id = request.POST.get("id")

    try:
        profile = Profile.objects.filter(user=request.user).first()
        medic = Profile.objects.filter(user__id=id).first()
        profile.favorites.add(medic.user)
        profile.save()
        msg = "Favorito adicionado com sucesso"
        _type = "success"
    except Exception as e:
        print("Erro %s" % e)
        msg = "Um erro ocorreu ao salvar o médico nos favoritos"
        _type = "danger"

    if page:
        arguments = "?page=%s" % (page)
    else:
        arguments = "?page=1"
    if name:
        arguments += "&name=%s" % name
    if speciality:
        arguments += "&specinality=%s" % speciality
    if neighborhood:
        arguments += "&neighborhood=%s" % neighborhood
    if city:
        arguments += "&city=%s" % city
    if state:
        arguments += "&state=%s" % state

    arguments += "&msg=%s&type=%s" % (msg, _type)

    return redirect(to='/medic/%s' % arguments)

def remove_favorite_view(request):
    page = request.POST.get("page")
    id = request.POST.get("id")

    try:
        profile = Profile.objects.filter(user=request.user).first()
        medic = Profile.objects.filter(user__id=id).first()
        profile.favorites.remove(medic.user)
        profile.save()
        msg = "Favorito removido com sucesso."
        _type = "success"
    except Exception as e:
        print("Erro %s" % e)
        msg = "Um erro ocorreu ao remover o médico nos favoritos."
        _type = "danger"


    if page:
        arguments = "?page=%s" % (page)
    else:
        arguments = "?page=1"
        arguments += "&msg=%s&type=%s" % (msg, _type)

    return redirect(to='/profile/%s' % arguments)
