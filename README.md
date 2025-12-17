# Proyecto Python - Django

Aplicación desarrollada con Django como ejercicio práctico del curso CoderHouse.
Permite registrar, listar y gestionar perros mediante vistas y templates.

---

## Funcionalidades
- Registrar perros
- Listar perros
- Ver detalle
- Actualizar y eliminar perros
- Autenticación de usuarios (login / logout)

---

## Requisitos
- Python 3.10+
- pip
- Virtualenv (recomendado)

---

## Instalación (Windows - PowerShell)

Clonar el repositorio y ubicarse en la carpeta del proyecto:

git clone https://github.com/luquini0/Django-Python.git
cd Python-Django

Crear y activar entorno virtual:

python -m venv .venv
.venv\Scripts\Activate.ps1

Si PowerShell bloquea la ejecución:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Instalar dependencias:

pip install -r requirements.txt

Aplicar migraciones:

python manage.py migrate

Crear superusuario (opcional):

python manage.py createsuperuser

---

## Ejecutar el proyecto

python manage.py runserver

Abrir en el navegador:

http://127.0.0.1:8000/

---

## Estructura del proyecto (resumen)

manage.py                utilidades de Django  
seguimiento/             configuración principal del proyecto  
inicio/                  app principal (modelos, vistas y templates)  
usuarios/                autenticación de usuarios  
templates/               templates globales  
db.sqlite3               base de datos local  
requirements.txt         dependencias  

---

## Rutas principales

/                       inicio  
/comprar-perro/          registrar perro  
/listar-perros/          listar perros  
/ver_perro/<id>/         detalle  
/actualizar_perro/<id>/  editar  
/eliminar_perro/<id>/    eliminar  
/usuarios/login/         login  
/usuarios/logout/        logout  

---

## Comandos útiles

Crear migraciones:

python manage.py makemigrations
python manage.py migrate

Ejecutar tests:

python manage.py test

---

Autor: Luquini0 
Curso: CoderHouse - Python / Django
