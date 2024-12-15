from django import views
from django.urls import path
from .views import NovelaDelete, LibroCreacion, NovelaDetalle, NovelaLista, OtroLista, OtroDetalle, NovelaUpdate, OtroUpdate, OtroDelete, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, HomeView, ComentarioPagina
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='base/logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

    path('listaNovelas/', NovelaLista.as_view(), name='novelas'),
    path('listaOtros/', OtroLista.as_view(), name='otros'),

    path('novelaDetalle/<int:pk>/', NovelaDetalle.as_view(), name='novela'),
    path('otroDetalle/<int:pk>/', OtroDetalle.as_view(), name='otro'),

    path('novelaEdicion/<int:pk>/', NovelaUpdate.as_view(), name='novela_editar'),
    path('otroEdicion/<int:pk>/', OtroUpdate.as_view(), name='otro_editar'),

    path('novelaBorrado/<int:pk>/', NovelaDelete.as_view(), name='novela_eliminar'),
    path('otroBorrado/<int:pk>/', OtroDelete.as_view(), name='otro_eliminar'),

    path('libroCreacion/', LibroCreacion.as_view(), name='nuevo'),

    path('novelaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('otroDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    path('acercaDeMi/', views.about, name='acerca_de_mi'),
]