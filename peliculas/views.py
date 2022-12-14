from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template.loader import get_template
from django.contrib.staticfiles import finders
from django.conf import settings

from .forms import formularioPersona, formularioPelicula, formularioPremio
from .models import tablaPersona, tablaPelicula, tablaPremio

from .insertar import *
from .convertir import *

import datetime
import os

from xhtml2pdf import pisa


# Create your views here.
class personaView(HttpRequest):

    def registrarPersona(request):
        persona = formularioPersona()
        
        return render(request, 'registrarPersona.html', {'form': persona})

    def procesarPersona(request):
        persona = formularioPersona(request.POST)
        
        if persona.is_valid():
            persona.save()
            
            #insertar registros en el archivo.txt
            insertar(persona.save())
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
        persona_sueldo_bajo = ''
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
        
        diferencia = sueldo_alto - sueldo_bajo
                

        return render(request, 'sueldos.html', 
            { 'sueldo_promedio': round(sueldo_promedio, 2),
              'sueldo_alto': sueldo_alto,
              'sueldo_bajo': sueldo_bajo,
              'datos_alto':persona_sueldo_alto,
              'datos_bajo':persona_sueldo_bajo,
              'diferencia': diferencia,
            }
        )

    def filtrar(request):
        encontrados = ''

        if 'nombre' in request.GET and 'dni' in request.GET:
            nombre = request.GET['nombre']
            dni = request.GET['dni']

        else:
            nombre = ''
            dni = 0
        
        encontrados = tablaPersona.objects.filter(nombre = nombre, dni = dni)
    
        return render(request, 'buscar.html', {'encontrados':encontrados, 'nombre':nombre, 'dni':dni})
    

    
    def sueldo_anual(request, sueldo):
        anual = sueldo * 12
    
        return render(request, 'anual.html', {'anual':anual})
    
    def edadActual(request, anio_nacimiento):
        fecha_atual = datetime.datetime.now()
        edad_actual = fecha_atual.year - anio_nacimiento

        return render(request, 'edadActual.html', {'actual': edad_actual})
    

    def actualizarSueldo(request, persona, sueldo, porcentaje):
        if porcentaje == 10:
            calculo = sueldo * 0.10
            final = sueldo + calculo
            person = tablaPersona.objects.filter(id=persona).update(sueldo_mensual = final)

        elif porcentaje == 15:
            calculo = sueldo * 0.15
            final = sueldo + calculo
            person = tablaPersona.objects.filter(id=persona).update(sueldo_mensual = final)

        else:
            if porcentaje == 20:
                calculo = sueldo * 0.20
                final = sueldo + calculo
                person = tablaPersona.objects.filter(id=persona).update(sueldo_mensual = final)
        
        personas = tablaPersona.objects.all()

        return render(request, 'listaPersonas.html', {'personas':personas})

    def consulta_join(request):
        pre = []
        pel = []

        premios = tablaPremio.objects.select_related('pelicula').all()
        peliculas = tablaPelicula.objects.select_related('persona').all()

        for premio in premios:
            p = premio.premio_ganador, premio.pelicula.nombre_pelicula
            pre.append(p)

        for pelicula in peliculas:
            p = pelicula.nombre_pelicula, pelicula.persona.nombre
            pel.append(p)

        return render(request, 'join.html', {'premios':pre, 'peliculas':pel})
    
    def leerInsert(request):
        archivo = leer()
        
        return render(request, 'leer.html', {'archivo':archivo})



class peliculaView(HttpRequest):

    def registrarPelicula(request):
        pelicula = formularioPelicula()
        
        return render(request, 'registrarPeliculas.html', {'formPelicula': pelicula})

    def procesarPelicula(request):
        pelicula = formularioPelicula(request.POST)
        
        if pelicula.is_valid():
            pelicula.save()
            insertar(pelicula.save())
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
            insertar(premio.save())
            premio = formularioPremio()
        
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



class imagenesView(HttpRequest):
    def imagenes(request):
        return render(request, 'imagenes.html')

    def convertir(request):
        if 'imagen' in request.GET:
            imagen = request.GET['imagen']
            convertida = conversion(imagen)
            tablaPremio.objects.filter(id=7).update(base = convertida)
        else:
            imagen = ''

        return render(request, 'imagenes.html', {'mensaje':'ok'})


def media(uri, rel):
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path

def get(request):

        personas = tablaPersona.objects.all()

        plantilla = get_template('pdf.html')

        lista = []
        contador_sueldos = 0
        sumatoria_sueldos = 0

        for i in personas:
            sueldo = i.sueldo_mensual
            contador_sueldos += 1
            sumatoria_sueldos += sueldo 
            lista.append(sueldo)
        
        mayor = max(lista)
        menor = min(lista)
        promedio = sumatoria_sueldos / contador_sueldos
        diferencia = mayor - menor

        contexto = {
            'personas':personas,
            'logo': 'img/logo.png',
            'sueldo_promedio': round(promedio,2),
            'sueldo_alto':mayor,
            'sueldo_bajo':menor,
            'diferencia':diferencia,
        }

        html = plantilla.render(contexto) 
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="archivo.pdf"'
        pisaStatus = pisa.CreatePDF(html, dest=response, link_callback=media)

        if pisaStatus.err:
            return HttpResponse('hubo un error')

        return response