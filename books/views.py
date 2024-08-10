from django.contrib import messages 
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.db.models import Q, OuterRef, Subquery, Max, Sum
from .models import *
from .forms import BookForm


# Create your views here.

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

def author_list_view(request):
    authors = Author.objects.all()  
    return render(request, 'author_list.html', {'authors': authors})

def add_author_view(request):
    context = {
        "autores": Author.objects.all(),
    }

    if request.method == 'POST':
        data = request.POST
        attributes = {
            "pseudonym": data.get('pseudonym'),  
        }
        
        if Author.objects.filter(pseudonym=attributes['pseudonym']).exists():
            messages.error(request, '¡El autor ya existe!', extra_tags="warning")
            return redirect('books:add_author')

        try:
            Author.objects.create(**attributes)
            messages.success(request, f'¡El autor: {attributes["pseudonym"]} ha sido creado satisfactoriamente!', extra_tags="success")
            return redirect('books:author_list')
        except Exception as e:
            messages.error(request, 'Hubo un error al crear el autor!', extra_tags="danger")
            print(e)
            return redirect('books:add_author')

    return render(request, "authorform.html", context=context)

def update_author_view(request, author_id):
    author = get_object_or_404(Author, id=author_id)

    if request.method == 'POST':
        author.pseudonym = request.POST.get('pseudonym')
        author.save()
        messages.success(request, 'Se ha actualizado el seudónimo correctamente.')
        return redirect('books:author_list')  

    return render(request, 'update_author.html', {'author': author})  

def delete_author_view(request, author_id):
    author = get_object_or_404(Author, id=author_id)

    if request.method == 'POST':
        author.delete()
        messages.success(request, 'Autor eliminado correctamente.')
        return redirect('books:author_list')

    return render(request, 'confirm_delete.html', {'author': author})

#book crud

def book_list_view(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, "book_list.html", context=context)



def add_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books:book_list')  # Redirige a la lista de libros después de agregar
    else:
        form = BookForm()
    
    return render(request, 'booksform.html', {'form': form})


def update_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:book_list')  # Redirige a la lista de libros después de actualizar
    else:
        form = BookForm(instance=book)

    return render(request, 'update_book.html', {'form': form, 'book': book})

def delete_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        messages.success(request, 'libro eliminado correctamente.')
        return redirect('books:book_list')

    return render(request, 'delete_book.html', {'book': book})

