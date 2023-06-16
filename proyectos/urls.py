from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index),
    # Gestion proyectos
    path('proyectos', views.proyectos),
    path('proyectos/<int:id_proyecto>', views.ver_proyecto),
    path("proyectos/update/<int:id_proyecto>", views.actualizar_proyecto),
    path("proyectos/delete/<int:id_proyecto>", views.eliminar_proyecto),

    # Barrios

    path('barrios', views.barrios),
    path("barrios/update/<int:id_barrio>", views.actualizar_barrio),
    path("barrios/delete/<int:id_barrio>", views.eliminar_barrio),
]
