from django.contrib import admin
from materiales.models import Deposito, Material, DepositoMaterial, Recepcion, ProyectoMaterial

# Register your models here.

admin.site.register(Deposito)
admin.site.register(Material)
admin.site.register(DepositoMaterial)
admin.site.register(Recepcion)
admin.site.register(ProyectoMaterial)
