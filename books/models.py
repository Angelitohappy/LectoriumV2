from django.db import models

# Create your models here.
class Author(models.Model):
    pseudonym = models.CharField(max_length=40, verbose_name='seudónimo')
    
    def __str__(self):
        return self.pseudonym
    
class Book(models.Model):
    isbn=models.CharField(max_length=14)
    title=models.CharField(max_length=40, verbose_name='titulo')
    synopsis=models.TextField(max_length=2000, verbose_name='sinopsis')
    publication_date=models.DateField(verbose_name='fecha de publicacion')
    front_page=models.FileField(verbose_name='portada')
    classification=models.FloatField(verbose_name='clasificacion')   
    authors=models.ManyToManyField(Author, related_name="autores")
    
    def __str__(self):
        return f'{self.title} - {str(self.publication_date)}' 