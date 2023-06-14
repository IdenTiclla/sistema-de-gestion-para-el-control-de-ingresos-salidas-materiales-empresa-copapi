from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.



class Administrador(AbstractUser):
    ci = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=8)
    domicilio = models.CharField(max_length=100)


    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='administrador_set',  # Nombre único para la relación inversa
        related_query_name='administrador'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='administrador_set',  # Nombre único para la relación inversa
        related_query_name='administrador'
    )

    fecha_creacion = models.DateField(auto_now=True)

    def is_admin(self):
        return True

    def is_encargado(self):
        return False




    class Meta:
        db_table = "Administrador"

    def __str__(self) -> str:
        return f"<User: {self.username}>"
    

class Encargado(AbstractUser):
    ci = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=8)
    domicilio = models.CharField(max_length=100)



    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='encargado_set',  # Nombre único para la relación inversa
        related_query_name='encargado'
    )


    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='encargado_set',  # Nombre único para la relación inversa
        related_query_name='encargado'
    )

    fecha_creacion = models.DateField(auto_now=True)

    def is_admin(self):
        return False

    def is_encargado(self):
        return True
    


    class Meta:
        db_table = "Encargado"

    def __str__(self) -> str:
        return f"<User: {self.username}>"
