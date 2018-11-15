from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from Sistema.models import *
from .serializers import MascotaSerializer
# Create your views here.

# class MascotaAgregar(APIView):
#     def post(self,request):
#             return render(request, "listarmascota.html", {'mascotas':mascotas, 'mascotacreada':True})
#         else:
#             form = UploadImageForm()
#         return render(request, "agregamascota.html", {'mascotas':mascotas, 'form':form})