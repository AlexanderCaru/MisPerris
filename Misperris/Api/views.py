from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from Sistema.models import *
from .serializers import MascotaSerializer
#Create your views here.

class UsuarioAgregar(APIView):
    def post(self,request):
        email = request.POST.get('email')
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        contra = request.POST.get('contra')
        contra2 = request.POST.get('contra2')
        fec_nac = request.POST.get('fec_nac')
        telefono = request.POST.get('telefono')
        region = request.POST.get('region')
        ciudad = request.POST.get('ciudad')
        tipo_viv = request.POST.get('tipo_viv')
        user = User.objects.create_user(username = rut, password= contra)
        user.save()
        return render(request, "index.html", {'creado':'si'})