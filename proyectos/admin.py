from django.contrib import admin
from proyectos.models import Barrio, Encargado, Proyecto, TipoServicio
# Register your models here.

admin.site.register(Barrio)
admin.site.register(Encargado)
admin.site.register(Proyecto)
admin.site.register(TipoServicio)
