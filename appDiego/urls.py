from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',index, name='inicio' ),

    path('buscar_clase/', buscarClase, name="buscar_clase" ),
    path('buscar2/', buscar2, name="buscar2" ),

    path('alumnos', AlumnoList.as_view(), name='alumnos' ),
    path('create_alumno', AlumnoCreate.as_view(), name='create_alumno' ),
    path('detail_alumno/<int:pk>', AlumnoDetail.as_view(), name='detail_alumno' ),
    path('update_alumno/<int:pk>', AlumnoUpdate.as_view(), name='update_alumno' ),
    path('delete_alumno/<int:pk>', AlumnoDelete.as_view(), name='delete_alumno' ),

    path('profesores/', ProfesorList.as_view(), name= "profesores"),
    path('create_profesor', ProfesorCreate.as_view(), name='create_profesor' ),
    path('detail_profesor/<int:pk>', ProfesorDetail.as_view(), name='detail_profesor' ),
    path('update_profesor/<int:pk>', ProfesorUpdate.as_view(), name='update_profesor' ),
    path('delete_profesor/<int:pk>', ProfesorDelete.as_view(), name='delete_profesor' ),

    path('clases/', ClaseList.as_view(), name= "clases"),
    path('create_clase', ClaseCreate.as_view(), name='create_clase' ),
    path('detail_clase/<int:pk>', ClaseDetail.as_view(), name='detail_clase' ),
    path('update_clase/<int:pk>', ClaseUpdate.as_view(), name='update_clase' ),
    path('delete_clase/<int:pk>', ClaseDelete.as_view(), name='delete_clase' ),

    path('sedes/', SedeList.as_view(), name= "sedes"),
    path('create_sede', SedeCreate.as_view(), name='create_sede' ),
    path('detail_sede/<int:pk>', SedeDetail.as_view(), name='detail_sede' ),
    path('update_sede/<int:pk>', SedeUpdate.as_view(), name='update_sede' ),
    path('delete_sede/<int:pk>', SedeDelete.as_view(), name='delete_sede' ),

    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name="appDiego/logout.html"), name='logout'),
    path('register/', register, name='register'),

    path('editar_usuario/', editarusuario, name='editar_usuario'),
    path('agregar_avatar/', agregarAvatar, name='agregar_avatar'),

    path('sobre_mi/', SobreMi, name="sobre_mi" ),
]

    