from django.db import models
from autenticacion.models import Encargado
# Create your models here.


class TipoServicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    fecha_creacion = models.DateField(auto_now=True)

    

    class Meta:
        db_table = "TipoServicio"

    def __str__(self) -> str:
        return f"<{self.nombre} - {self.descripcion}>"

    
class Barrio(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)

    fecha_creacion = models.DateField(auto_now=True)


    class Meta:
        db_table = "Barrio"

    def __str__(self) -> str:
        return f"<{self.nombre} - {self.ubicacion}>"
    

class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)

    tipo = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)
    encargado = models.ForeignKey(Encargado, on_delete=models.CASCADE)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)

    fecha_creacion = models.DateField(auto_now=True)



    class Meta:
        db_table = "Proyecto"

    def __str__(self) -> str:
        return f"<{self.nombre} - {self.tipo.nombre} - {self.encargado.first_name} - {self.barrio.nombre}>"