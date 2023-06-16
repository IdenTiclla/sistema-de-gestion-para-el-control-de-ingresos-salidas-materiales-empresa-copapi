from django.urls import path

from . import views

urlpatterns = [
    # Gestion materiales
    path('materiales', views.materiales),
    path("materiales/update/<int:id_material>", views.actualizar_material),
    path("materiales/delete/<int:id_material>", views.eliminar_material),
    # Gestion Depositos

    path('depositos', views.depositos),
    path("depositos/update/<int:id_deposito>", views.actualizar_deposito),
    path("depositos/delete/<int:id_deposito>", views.eliminar_deposito),
]
