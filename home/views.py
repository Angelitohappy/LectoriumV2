from django import views
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages
from .models import User
from books.models import Book
from books.views import book_list_view

# Create your views here.
def my_home(request):
    # Obtener todos los libros de la base de datos
    books = Book.objects.all()
    # Renderizar la plantilla con la lista de libros
    return render(request, 'home.html', {'books': books})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username, password=password)
            messages.success(request, f'¡Bienvenido, {user.username}!')
            return redirect('home:home') 
        except User.DoesNotExist:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'login.html') 

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return redirect('home:register') 

        new_user = User(username=username, email=email, password=password)
        new_user.save()
        messages.success(request, '¡Usuario creado satisfactoriamente! Puedes iniciar sesión.')
        return redirect('home.login')  

    return render(request, 'register.html') 
