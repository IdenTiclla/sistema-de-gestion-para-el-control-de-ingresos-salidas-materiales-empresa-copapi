from django.shortcuts import render

from django.http import HttpResponse
# autenticacion
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Administrador, Encargado

# para los mensajes
from django.contrib import messages


# Create your views here.


def index_view(request):
    return HttpResponse("hello world")


@login_required
def index_view(request):

    cliente = request.user

    return render(request, "index.html", {})

def register_page(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('index_page')
        return render(request, "register.html")
    elif request.method == "POST":
        print(request.POST)
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        ci = request.POST['ci']
        telefono = request.POST['telefono']
        email = request.POST['email']
        domicilio = request.POST['domicilio']

        
        username = request.POST['username']
        password = request.POST['password']
        password_again = request.POST['password_again']

        if password != password_again:
            return HttpResponse("Las contraseñas no coinciden...")
        
        rol = request.POST['rol']

        if rol == 'Administrador':
            new_user = Administrador.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                ci=ci,
                telefono=telefono,
                email=email,
                username=username,
                password=password,
                domicilio=domicilio
            )

        elif rol == 'Encargado':
            new_user = Encargado.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                ci=ci,
                telefono=telefono,
                email=email,
                username=username,
                password=password,
                domicilio=domicilio

            )

        if rol == "Administrador":
            new_user.is_superuser = True
            new_user.is_staff = True

        new_user.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Usuario creado correctamente!")
        return render(request, "login.html")


def login_page(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('index_page')
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Autenticación exitosa
            login(request, user)
            return redirect('index_page')
        else:
            # Credenciales incorrectas
            messages.error(request, "Credenciales incorrectas")
            return redirect('login_page')
        

def logout_view(request):
    logout(request)
    return redirect('login_page')