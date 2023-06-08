from django.db import models
# Create your models here.


class TipoServicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    fecha_creacion = models.DateField(auto_now=True)

    

    class Meta:
        db_table = "TipoServicio"

    def __str__(self) -> str:
        return f"<{self.nombre} - {self.descripcion}>"


class Encargado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    ci = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)


    fecha_creacion = models.DateField(auto_now=True)

    

    class Meta:
        db_table = "Encargado"

    def __str__(self) -> str:
        return f"<{self.nombre} - {self.apellido_paterno} - {self.apellido_materno}>"
    
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
    encargado = models.OneToOneField(Encargado, on_delete=models.CASCADE)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)

    fecha_creacion = models.DateField(auto_now=True)



    class Meta:
        db_table = "Proyecto"

    def __str__(self) -> str:
        return f"<{self.nombre} - {self.tipo.nombre} - {self.encargado.nombre} - {self.barrio.nombre}>"