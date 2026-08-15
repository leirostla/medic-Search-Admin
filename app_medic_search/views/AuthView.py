from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app_medic_search.models.profile import Profile
from app_medic_search.forms.AuthForm import LoginForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import hashlib

def login_view(request):
    loginForm = LoginForm()
    message = None
    
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                _next = request.GET.get('next')
                if _next is not None:
                    return redirect(_next)
                else:
                    return redirect("/")
            else:
                message = {
                    'type': 'danger',
                    'text': 'Dados de usuário incorretos'
                }

    context = {
        'form': loginForm,
        'message': message,
        'title': 'Login',
        'button_text': 'Entrar',
        'link_text': 'Registrar',
        'link_href': '/register'
    }

    print('ABC ABC ABC')
    return render(request, template_name='auth/auth.html', context=context, status=200)