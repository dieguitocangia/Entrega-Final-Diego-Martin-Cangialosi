1) Creo una carpeta llamada ENTREGA FINAL en mi disco local
2) Abro la terminal y escribo "django-admin startproject ProyectoDiego ." para dar inicio al proyecto y tener asi un paquete llamado "ProyectoDiego" y un archivo manage.py
3) En la terminal escribo "python manage.py migrate" para crear la base de datos.
4) En la terminal escribo "python manage.py runserver" para levantar el servidor web.
5) Creo mi aplicación utilizando el comando "django-admin startapp"
6) Importo HttpResponse de django.http en mi archivo views.py
7) Importo Template y Context desde django.template en mi archivo views.py
8) Agrego la aplicación en settings.py
9) Cambio el nombre a mi base de datos a "gimansio.db" desde settings.py
10) Cambio el idioma del proyecto a "es" desde settings.py
11) Cambio el time zone a America/Argentina/Buenos Aires desde settings.py
12) Defino una ruta para appDiego desde el archivo urls.py del proyecto. Esta ruta va a ser path('appDiego/', include('appDiego.urls'))
13) Importo include en urls.py from django.urls
14) Creo el archivo urls.py dentro del paquete appDiego.
12) En el archivo models.py dentro del paquete de la aplicación creo tres clases: 
	Clase con atributos nombre y horario.
	Alumno con atributos nombre, apellido y email.
	Profesor con atributos nombre, apellido, email y clase a cargo.
	Sede con atributos nombre, direccion, horarios de atencion y servicios que ofrece.
13) Creo los modelos y luego los subo a la base de datos utilizando los comandos "python manage.py makemigrations" y "python manage.py migrate" respectivamente.
14) Agrego algunos datos a la clase "Clase" desde DB Browser.
15) Descargo template desde bootstrap.
16) Creo carpeta static dentro del paquete appDiego y otra carpeta llamada appDiego dentro de la carpeta static.
17) Pego las carpetas assets, js y css del template dentro de la carpeta static/appDiego.
18) Creo carpeta templates dentro de appDiego y otra carpeta llamada appDiego dentro de templates.
19) Pego el index.html en la carpeta templates con el nombre base.html
20) Defino funcion index en views.py
21) Cargo los archivos estaticos en base.html usando {% load static %}
22) Creo los html para cada clase
23) Creo las rutas para los html de cada clase desde urls.py
24) Creo un bloque en base.html para despues poder heredarlo al html de cada clase utilizando {% extends 'appDiego/base.html' %}
25) Creo superuser. Usuario admin - Contraseña 12345
26) Importo todos los modelos en el archivo admin.py dentro del paquete de la aplicación para poder modificarlos desde el panel de Administración.
27) Creo el archivo forms.py dentro de la aplicación, que contiene el import de forms desde django.
28) Utilizando modelos basados en vistas desarrollo todas las views, urls y archivos html para lograr el concepto CRUD en cada uno de los modelos.
29) Utilizando funciones como login_request, register y editar usuario desarrollo toda la parte de login, logout, registrar y editar usuarios.
30) Utilizando la funcion agregar Avatar agrego esa funcionalidad a mi aplicación.