from django.shortcuts import render, redirect

from django.contrib import messages

from materiales.models import Material
# Create your views here.


# Gestion materiales
def materiales(request):
    if request.method == "GET":
        materiales = Material.objects.all()
        return render(request, "materiales/materiales.html", {
            'materiales': materiales,
        })
    
    elif request.method == "POST":
        print(request.POST)
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']

        material = Material.objects.filter(nombre=nombre)
        if material:
            messages.add_message(request=request, level=messages.SUCCESS, message="El material ya existe")
            return redirect('/materiales')
        else:
            material = Material(nombre=nombre, descripcion=descripcion)
            material.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Material agregado correctamente!")
        
        return redirect('/materiales')
    

def actualizar_material(request, id_material):
    material = Material.objects.get(id=id_material)

    if request.method == "GET":
        return render(request, "materiales/actualizar_material.html", {
            'material': material,
        })
    
    elif request.method == "POST":

        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']


        aux_material = Material.objects.filter(nombre=nombre)
        if aux_material and material.nombre != nombre:
            messages.add_message(request=request, level=messages.SUCCESS, message="El material ya existe!")
            return redirect('/materiales')
        else:
            material.nombre = nombre
            material.descripcion = descripcion
            material.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Material Actualizado correctamente!")
        

        return redirect('/materiales')


def eliminar_material(request, id_material):
    material = Material.objects.get(id=id_material)
    material.delete()

    messages.add_message(request=request, level=messages.SUCCESS, message="Material Eliminado exitosamente!")

    return redirect("/materiales")