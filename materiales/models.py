from django.db import models
from proyectos.models import Proyecto
from transportes.models import Transporte

# Create your models here.

class Deposito(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)


    fecha_creacion = models.DateField(auto_now=True)


    class Meta:
        db_table = "Deposito"

    def __str__(self) -> str:
        return f"<{self.nombre} - {self.ubicacion}>"
    
    def agregar_material(self, material):
        deposito_material = DepositoMaterial.objects.filter(deposito=self, material=material)
        if deposito_material:
            print("ya existe el material en ese deposito")

class Material(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)


    class Meta:
        db_table = "Material"

    def __str__(self) -> str:
        return f"<{self.nombre} - {self.descripcion}>"
    

class DepositoMaterial(models.Model):
    deposito = models.ForeignKey(Deposito, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    cantidad = models.PositiveIntegerField()


    class Meta:
        db_table = "DepositoMaterial"
        unique_together = ('deposito', 'material') # no permitira ingresar el mismo material en el mismo deposit

    def __str__(self) -> str:
        return f"<{self.deposito.nombre} - {self.material.nombre} - {self.cantidad}>"
    

# nucleo


class Recepcion(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now=True)


    class Meta:
        db_table = "Recepcion"

    def __str__(self) -> str:
        return f"<{self.nombre}>"
    

# proyecto material

class ProyectoMaterial(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    recepcion = models.ForeignKey(Recepcion, on_delete=models.CASCADE)
    transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE)


    cantidad = models.PositiveIntegerField()

    class Meta:
        db_table = "ProyectoMaterial"

    def __str__(self) -> str:
        return f"<{self.proyecto.nombre} {self.material.nombre} {self.cantidad}>"