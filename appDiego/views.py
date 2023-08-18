from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'appDiego/base.html')

@login_required
def buscarClase(request):
    return render(request,'appDiego/buscarClase.html')

@login_required
def SobreMi(request):
    return render(request,'appDiego/sobremi.html')

@login_required
def buscar2(request):
    if request.GET['clase']:
        clase=request.GET['clase']
        horarios= Clase.objects.filter(nombre__icontains=clase)
        return render(request, "appDiego/resultadosClase.html",{"clases": clase, "horarios": horarios })
    return HttpResponse("No se ingresaron datos para buscar")

class AlumnoList(LoginRequiredMixin,ListView):
    model = Alumno

class AlumnoCreate(LoginRequiredMixin,CreateView):
    model = Alumno
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('alumnos')

class AlumnoDetail(LoginRequiredMixin,DetailView):
    model = Alumno

class AlumnoUpdate(LoginRequiredMixin,UpdateView):
    model = Alumno
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('alumnos')

class AlumnoDelete(LoginRequiredMixin,DeleteView):
    model = Alumno
    success_url = reverse_lazy('alumnos')

class ProfesorList(LoginRequiredMixin,ListView):
    model = Profesor

class ProfesorCreate(LoginRequiredMixin,CreateView):
    model = Profesor
    fields = ['nombre', 'apellido', 'email', 'clase_a_cargo']
    success_url = reverse_lazy('profesores')

class ProfesorDetail(LoginRequiredMixin,DetailView):
    model = Profesor

class ProfesorUpdate(LoginRequiredMixin,UpdateView):
    model = Profesor
    fields = ['nombre', 'apellido', 'email', 'clase_a_cargo']
    success_url = reverse_lazy('profesores')

class ProfesorDelete(LoginRequiredMixin,DeleteView):
    model = Profesor
    success_url = reverse_lazy('profesores')

class ClaseList(LoginRequiredMixin,ListView):
    model = Clase

class ClaseCreate(LoginRequiredMixin,CreateView):
    model = Clase
    fields = ['nombre', 'horario']
    success_url = reverse_lazy('clases')

class ClaseDetail(LoginRequiredMixin,DetailView):
    model = Clase

class ClaseUpdate(LoginRequiredMixin,UpdateView):
    model = Clase
    fields = ['nombre', 'horario']
    success_url = reverse_lazy('clases')

class ClaseDelete(LoginRequiredMixin,DeleteView):
    model = Clase
    success_url = reverse_lazy('clases')

class SedeList(LoginRequiredMixin,ListView):
    model = Sede

class SedeCreate(LoginRequiredMixin,CreateView):
    model = Sede
    fields = ['nombre', 'direccion', 'horarios_de_atencion', 'servicios']
    success_url = reverse_lazy('sedes')

class SedeDetail(LoginRequiredMixin,DetailView):
    model = Sede

class SedeUpdate(LoginRequiredMixin,UpdateView):
    model = Sede
    fields = ['nombre', 'direccion', 'horarios_de_atencion', 'servicios']
    success_url = reverse_lazy('sedes')

class SedeDelete(LoginRequiredMixin,DeleteView):
    model = Sede
    success_url = reverse_lazy('sedes')

def login_request(request):
    if request.method == 'POST':
        loginform = AuthenticationForm(request, data=request.POST)
        if loginform.is_valid():
            usuario = loginform.cleaned_data.get('username')
            clave = loginform.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render (request,"appDiego/base.html", {"mensaje": f"Bienvenido {usuario} al Sitio Web Oficial de Training Center"})
            else:
                return render (request, "appDiego/login.html", {"form":loginform, "mensaje": "Usd. no ha ingresado los datos correctamente"})
        else:
            return render (request, "appDiego/login.html", {"form":loginform, "mensaje": "Usd. no ha ingresado los datos correctamente"})
    
    loginform=AuthenticationForm()

    return render (request, "appDiego/login.html", {"form":loginform})

def register(request):
    if request.method == "POST":
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, 'appDiego/base.html', {"mensaje": "Usuario creado correctamente"})
    else: 
        form = RegistroUsuariosForm()
    return render(request,"appDiego/registro.html", {"form": form})

@login_required
def editarusuario(request):
    usuario = request.user
    if request.method=="POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "appDiego/base.html", {'mensaje': f"El Usuario {usuario.username} se ha actualizado correctamente."})
        else:
            return render(request, "appDiego/editarusuario.html", {'form': form}) 
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "appDiego/editarusuario.html", {'form': form, 'usuario':usuario.username}) 

@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            oldavatar = Avatar.objects.filter(user=u)
            if len(oldavatar) > 0:
                 oldavatar[0].delete()
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar']=imagen
            return render(request, "appDiego/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "appDiego/agregarAvatar.html", {'form': form}) 