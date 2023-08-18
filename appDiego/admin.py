from django.contrib import admin
from .models import Clase, Profesor, Alumno, Sede, Avatar

# Register your models here.

admin.site.register(Clase)
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Sede)
admin.site.register(Avatar)