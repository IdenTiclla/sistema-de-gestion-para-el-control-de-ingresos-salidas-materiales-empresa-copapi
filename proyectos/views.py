from django.shortcuts import render, redirect

from django.contrib import messages

from autenticacion.models import Encargado
from proyectos.models import Proyecto, TipoServicio, Barrio
# Create your views here.

# Gestion proyectos
def proyectos(request):
    if request.method == "GET":
        proyectos = Proyecto.objects.all()
        encargados = Encargado.objects.all()
        tipo_servicios = TipoServicio.objects.all()
        barrios = Barrio.objects.all()
        print(encargados)
        return render(request, "proyectos/proyectos.html", {
            'proyectos': proyectos,
            'encargados': encargados,
            'tipo_servicios': tipo_servicios,
            'barrios': barrios
        })
    
    elif request.method == "POST":
        print(request.POST)
        nombre = request.POST['nombre']
        id_encargado = request.POST['id_encargado']
        id_tipo_servicio = request.POST['id_tipo_servicio']
        id_barrio = request.POST['id_barrio']

        encargado = Encargado.objects.get(id=id_encargado)
        tipo_servicio = TipoServicio.objects.get(id=id_tipo_servicio)
        barrio = Barrio.objects.get(id=id_barrio)
        print(encargado)
        print(tipo_servicio)
        print(barrio)

        proyecto = Proyecto.objects.filter(tipo=tipo_servicio, barrio=barrio)
        if proyecto:
            messages.add_message(request=request, level=messages.SUCCESS, message="El barrio ya tiene un proyecto con ese tipo de servicio")
            return redirect('/proyectos')
        else:
            proyecto = Proyecto(nombre=nombre, encargado=encargado, tipo=tipo_servicio, barrio=barrio)
            proyecto.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Proyecto agregado correctamente!")
        
        return redirect('/proyectos')

        

def ver_proyecto(request, id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)
    print(proyecto)
    return render(request, "proyectos/ver_proyecto.html", {
        'proyecto': proyecto,
    })
    
def actualizar_proyecto(request, id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)

    if request.method == "GET":
        return render(request, "proyecto/actualizar_proyecto.html", {
            'proyecto': proyecto,
        })
    
    elif request.method == "POST":

        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        

        proyecto.nombre = nombre
        proyecto.descripcion = descripcion


        proyecto.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Proyecto Actualizado exitosamente!")
        return redirect('/proyectos')


def eliminar_proyecto(request, id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)
    proyecto.delete()

    messages.add_message(request=request, level=messages.SUCCESS, message="Proyecto Eliminado exitosamente!")

    return redirect("/proyecto")



# Gestion Barrios
def barrios(request):
    if request.method == "GET":
        barrios = Barrio.objects.all()

        print(barrios)
        return render(request, "barrios/barrios.html", {
            'barrios': barrios
        })
    
    elif request.method == "POST":
        print(request.POST)
        nombre = request.POST['nombre']
        ubicacion = request.POST['ubicacion']

        barrio = Barrio.objects.filter(nombre=nombre)
        if barrio:
            messages.add_message(request=request, level=messages.SUCCESS, message="Barrio ya existente!")
            return redirect('/barrios')
        else:
            barrio = Barrio(nombre=nombre, ubicacion=ubicacion)
            barrio.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Barrio agregado correctamente!")
        
        return redirect('/barrios')

        
    
def actualizar_barrio(request, id_barrio):
    barrio = Barrio.objects.get(id=id_barrio)

    if request.method == "GET":
        return render(request, "barrios/actualizar_barrio.html", {
            'barrio': barrio,
        })
    
    elif request.method == "POST":

        nombre = request.POST['nombre']
        ubicacion = request.POST['ubicacion']
    
        barrio.nombre = nombre
        barrio.ubicacion = ubicacion


        barrio.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Barrio Actualizado exitosamente!")
        return redirect('/barrios')


def eliminar_barrio(request, id_barrio):
    barrio = Barrio.objects.get(id=id_barrio)
    barrio.delete()

    messages.add_message(request=request, level=messages.SUCCESS, message="Barrio Eliminado exitosamente!")

    return redirect("/barrios")


