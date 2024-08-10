from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=40, verbose_name='Nombre de Usuario')
    email = models.EmailField(max_length=254, verbose_name='correo')
    password = models.CharField(max_length=16, verbose_name='contraseña')
    
    def __str__(self):
        return f'{self.username} - {self.email}'
    
