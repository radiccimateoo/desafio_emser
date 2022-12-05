from django.urls import path
from .views import personaView, peliculaView, premioView

urlpatterns = [

    path('registrarPersona/', personaView.registrarPersona, name='registrar'),
    path('guardarPersona/', personaView.procesarPersona, name='guardar'),
    path('', personaView.listarPersona, name='listaPersonas'),
    path('editarPersona/<int:id_persona>', personaView.editarPersona, name='editar'),
    path('actualizarPersona/<int:id_persona>', personaView.actulizarPersona, name='actualizar'),
    path('eliminarPersona/<int:id_persona>', personaView.eliminarPersona, name='eliminar'),


    path('registrarPelicula/', peliculaView.registrarPelicula, name='registrarPelicula'),
    path('guardarPelicula/', peliculaView.procesarPelicula, name='guardarPelicula'),
    path('listaPeliculas/', peliculaView.listarPelicula, name='listaPeliculas'),
    path('editarPelicula/<int:id_pelicula>', peliculaView.editarPelicula, name='editarPelicula'),
    path('actualizarPelicula/<int:id_persona>', peliculaView.actulizarPelicula, name='actualizarPelicula'),
    path('eliminarPelicula/<int:id_persona>', peliculaView.eliminarPelicula, name='eliminarPelicula'),


    path('registrarPremio/', premioView.registrarPremio, name='registrarPremio'),
    path('guardarPremio/', premioView.procesarPremio, name='guardarPremio'),
    path('listaPremios/', premioView.listarPremio, name='listaPremios'),
    path('editarPremio/<int:id_premio>', premioView.editarPremio, name='editarPremio'),
    path('actualizarPremio/<int:id_premio>', premioView.actulizarPremio, name='actualizarPremio'),
    path('eliminarPremio/<int:id_premio>', premioView.eliminarPremio, name='eliminarPremio'),

]