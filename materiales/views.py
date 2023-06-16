from django.shortcuts import render, redirect

from django.contrib import messages

from materiales.models import Material, Deposito
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

# Gestion depositos

def depositos(request):
    if request.method == "GET":
        depositos = Deposito.objects.all()
        return render(request, "depositos/depositos.html", {
            'depositos': depositos,
        })
    
    elif request.method == "POST":
        print(request.POST)
        nombre = request.POST['nombre']
        ubicacion = request.POST['ubicacion']

        deposito = Deposito.objects.filter(nombre=nombre)
        if deposito:
            messages.add_message(request=request, level=messages.SUCCESS, message="El Deposito ya existe")
            return redirect('/depositos')
        else:
            deposito = Deposito(nombre=nombre, ubicacion=ubicacion)
            deposito.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Deposito agregado correctamente!")
        
        return redirect('/depositos')
    

def actualizar_deposito(request, id_deposito):
    deposito = Deposito.objects.get(id=id_deposito)

    if request.method == "GET":
        return render(request, "depositos/actualizar_deposito.html", {
            'deposito': deposito,
        })
    
    elif request.method == "POST":

        nombre = request.POST['nombre']
        ubicacion = request.POST['ubicacion']


        aux_deposito = Deposito.objects.filter(nombre=nombre)
        if aux_deposito and deposito.nombre != nombre:
            messages.add_message(request=request, level=messages.SUCCESS, message="El deposito ya existe!")
            return redirect('/depositos')
        else:
            deposito.nombre = nombre
            deposito.ubicacion = ubicacion
            deposito.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Deposito Actualizado correctamente!")
        

        return redirect('/depositos')


def eliminar_deposito(request, id_deposito):
    deposito = Deposito.objects.get(id=id_deposito)
    deposito.delete()

    messages.add_message(request=request, level=messages.SUCCESS, message="Deposito Eliminado exitosamente!")

    return redirect("/depositos")