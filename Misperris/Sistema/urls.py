from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns=[
    path('',views.index, name="index"),
    path('agregapersona',views.agregapersona, name="agregapersona"),
    path('agregamascota',views.agregamascota, name="agregamascota"),
    path('servicios',views.servicios, name="servicios"),
    path('ingresar',views.ingresar, name="ingresar"),
    url('salir',views.salir,name="salir"),
    path('listarmascota',views.listarmascota, name="listarmascota"),
    path('recuperarpasswd',views.recuperarpasswd, name="recuperarpasswd"),
    path('recuperarpasswd2',views.recuperarpasswd2, name="recuperarpasswd2"),
    path('galeria',views.galeria, name="galeria"),
    ]