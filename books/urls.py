from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'books'  

urlpatterns = [
    path('author_list/', author_list_view, name='author_list'),
    path('add_author/', add_author_view, name='add_author'),
    path('update_author/<int:author_id>', update_author_view, name='update_author'),
    path('delete_author/<int:author_id>', delete_author_view, name='delete_author'),
    
    path('book_list/', book_list_view, name='book_list') ,
    path('add_book/', add_book_view, name='add_book'),
    path('update_book/<int:book_id>', update_book_view, name='update_book'),
    path('delete_book/<int:book_id>', delete_book_view, name='delete_book'),
    
    path('book/<int:book_id>/', book_detail, name='book_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)