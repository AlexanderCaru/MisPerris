from django.conf.urls import url
from . import views
urlpatterns=[
    url('UsuarioAgregar/', views.UsuarioAgregar.as_view()),
]