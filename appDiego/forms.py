from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClaseFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre de la Clase", max_length=50, required=True)
    horario = forms.TimeField(label="Horario de la Clase", required=True)

class RegistroUsuariosForm(UserCreationForm):
    first_name=forms.CharField(label="Nombre/s",max_length=50, required=False)
    last_name=forms.CharField(label="Apellido/s", max_length=50, required=False)
    email=forms.EmailField(label="Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}    

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name=forms.CharField(label="Apellido/s", max_length=50, required=False)

    class Meta:
        model=User
        fields=['first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}    

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)