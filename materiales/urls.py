from django.urls import path

from . import views

urlpatterns = [
    # Gestion materiales
    path('materiales', views.materiales),
    path("materiales/update/<int:id_material>", views.actualizar_material),
    path("materiales/delete/<int:id_material>", views.eliminar_material),
    # Barrios
]
