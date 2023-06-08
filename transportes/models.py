from django.db import models

# Create your models here.


class Chofer(models.Model):

    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)

    licencia = models.CharField(max_length=50)
    ci = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)

    class Meta:
        db_table = "Chofer"

    def __str__(self) -> str:
        return f"<{self.nombre} - {self.apellido_paterno} - {self.apellido_materno}>"


class Vehiculo(models.Model):
    tipo = models.CharField(max_length=50)
    placa = models.CharField(max_length=50)

    class Meta:
        db_table = "Vehiculo"

    def __str__(self) -> str:
        return f"<{self.tipo} - {self.placa}>"
    

class Transporte(models.Model):
    chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now=True)

    class Meta:
        db_table = "Transporte"

    def __str__(self) -> str:
        return f"<{self.chofer.nombre} - {self.vehiculo.tipo} - {self.fecha_creacion}>"