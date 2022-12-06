from django.shortcuts import render
from django.http import HttpRequest

from .forms import formularioPersona, formularioPelicula, formularioPremio
from .models import tablaPersona, tablaPelicula, tablaPremio

# Create your views here.
class personaView(HttpRequest):

    def registrarPersona(request):
        persona = formularioPersona()
        
        return render(request, 'registrarPersona.html', {'form': persona})

    def procesarPersona(request):
        persona = formularioPersona(request.POST)
        
        if persona.is_valid():
            persona.save()
            persona = formularioPersona()
        
        return render(request, 'registrarPersona.html', {'form':persona, 'mensaje':'ok'})

    def editarPersona(request, id_persona):
        persona = tablaPersona.objects.filter(id= id_persona).first()
        form = formularioPersona(instance= persona)
        
        return render(request, 'editarPersona.html', {'form':form, 'persona':persona})

    def listarPersona(request):
        persona = tablaPersona.objects.all()

        return render(request, 'listaPersonas.html', {'personas':persona})

    def actulizarPersona(request, id_persona):
        persona =tablaPersona.objects.get(pk=id_persona)
        form = formularioPersona(request.POST, instance= persona)
        
        if form.is_valid():
            form.save()
        
        personas = tablaPersona.objects.all()

        return render(request, 'listaPersonas.html', {'personas': personas})

    def eliminarPersona(request, id_persona):
        persona = tablaPersona.objects.get(pk=id_persona)
        persona.delete()
        personas = tablaPersona.objects.all()

        return render(request, 'listaPersonas.html', {'personas': personas, 'mensaje':'ok'})
    

    def funciones_sueldos(request):
        datos = tablaPersona.objects.all()
        suma = 0
        cantidad_sueldos = 0
        persona_sueldo_bajo = None #verificar error
        sueldo_alto = datos[0].sueldo_mensual
        sueldo_bajo = datos[0].sueldo_mensual

        # calcular el promedio de los sueldos
        for sueldo in datos:
            suma += sueldo.sueldo_mensual
            cantidad_sueldos += 1

        sueldo_promedio = suma / cantidad_sueldos

        # calcular sueldo mas alto y obtener datos
        for dato in datos:
            if dato.sueldo_mensual > sueldo_alto:
                sueldo_alto = dato.sueldo_mensual
                persona_sueldo_alto = dato.nombre.capitalize(), dato.apellido.capitalize(), dato.dni
        
        # calcular sueldo mas bajo y obtener datos
        for dato in datos:
            if dato.sueldo_mensual < sueldo_bajo:
                sueldo_bajo = dato.sueldo_mensual
                persona_sueldo_bajo = dato.nombre.capitalize(), dato.apellido.capitalize(), dato.dni
                

        return render(request, 'listaPersonas.html', 
            { 'sueldo_promedio': round(sueldo_promedio, 2),
              'sueldo_alto': sueldo_alto,
              'sueldo_bajo': sueldo_bajo,
              'datos_alto':persona_sueldo_alto,
              'datos_bajo':persona_sueldo_bajo
            }
        )


class peliculaView(HttpRequest):

    def registrarPelicula(request):
        pelicula = formularioPelicula()
        
        return render(request, 'registrarPeliculas.html', {'formPelicula': pelicula})

    def procesarPelicula(request):
        pelicula = formularioPelicula(request.POST)
        
        if pelicula.is_valid():
            pelicula.save()
            pelicula = formularioPelicula()
        
        return render(request, 'registrarPeliculas.html', {'formPelicula':pelicula, 'mensaje':'ok'})

    def editarPelicula(request, id_pelicula):
        pelicula = tablaPelicula.objects.filter(id= id_pelicula).first()
        formPelicula = formularioPelicula(instance= pelicula)
        
        return render(request, 'editarPelicula.html', {'formPelicula':formPelicula, 'pelicula':pelicula})

    def listarPelicula(request):
        pelicula = tablaPelicula.objects.all()

        return render(request, 'listaPeliculas.html', {'peliculas':pelicula})

    def actulizarPelicula(request, id_pelicula):
        pelicula =tablaPelicula.objects.get(pk=id_pelicula)
        formPelicula = formularioPelicula(request.POST, instance= pelicula)
        
        if formPelicula.is_valid():
            formPelicula.save()
        
        peliculas = tablaPelicula.objects.all()

        return render(request, 'listaPeliculas.html', {'peliculas': peliculas})

    def eliminarPelicula(request, id_pelicula):
        pelicula = tablaPelicula.objects.get(pk=id_pelicula)
        pelicula.delete()
        peliculas = tablaPelicula.objects.all()

        return render(request, 'listaPeliculas.html', {'peliculas': peliculas, 'mensaje':'ok'})

        
class premioView(HttpRequest):
    def registrarPremio(request):
        premio = formularioPremio()
        
        return render(request, 'registrarPremios.html', {'formPremio': premio})

    def procesarPremio(request):
        premio = formularioPremio(request.POST)
        
        if premio.is_valid():
            premio.save()
            premio = formularioPelicula()
        
        return render(request, 'registrarPremios.html', {'formPremio':premio, 'mensaje':'ok'})

    def editarPremio(request, id_premio):
        premio = tablaPremio.objects.filter(id= id_premio).first()
        formpremio = formularioPremio(instance= premio)
        
        return render(request, 'editarPremio.html', {'formPremio':formpremio, 'premio':premio})

    def listarPremio(request):
        premio = tablaPremio.objects.all()

        return render(request, 'listaPremios.html', {'premios':premio})

    def actulizarPremio(request, id_premio):
        premio =tablaPremio.objects.get(pk=id_premio)
        formPremio = formularioPremio(request.POST, instance= premio)
        
        if formPremio.is_valid():
            formPremio.save()
        
        premios = tablaPremio.objects.all()

        return render(request, 'listaPremios.html', {'premios': premios})

    def eliminarPremio(request, id_premio):
        premio = tablaPremio.objects.get(pk=id_premio)
        premio.delete()
        premios = tablaPremio.objects.all()

        return render(request, 'listaPremios.html', {'premios': premios, 'mensaje':'ok'})