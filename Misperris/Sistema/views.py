from django.shortcuts import render, render_to_response, redirect
from .models import Persona, Mascota
from django.template import loader,RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from .forms import ContactoForm
from django.core.mail import EmailMessage, send_mail

# Create your views here.
def index(request):
    personas=Persona.objects.all()
    mascotas=Mascota.objects.all()
    plantilla=loader.get_template("index.html")
    contexto={
        'mascotas':mascotas,
        'personas':personas
    }
    return HttpResponse(plantilla.render(contexto,request))

def agregapersona(request):
    return render(request, "agregapersona.html")

def recuperarpasswd(request):
    form=RecuperarPasswd(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data        
        persona=Persona.objects.get(codigoPersona=data.get("codigoPersona"))
        correo=persona.correoPersona
        send_mail('Recuperar Contraseña','','busys1234@gmail.com',[correo],html_message='<a href="http://localhost:8000/recuperarpasswd2?user='+persona.codigoPersona+'">aaa</a>')
       

    return render(request, "recuperarpasswd.html",{'form':form})
def recuperarpasswd2(request):
    form=RetypePasswd(request.POST or None)
    x=False
    mensaje=""
    if form.is_valid():
        data=form.cleaned_data        
        if data.get("passwd") == data.get("passwd2"):
            try:
                user=User.objects.get(username=request.GET.get("user"))
                user.set_password(data.get("passwd"))
                user.save()
                mensaje="contraseña cambiada correctamente"
            except:
                mensaje="Este usuario no existe, REINTENTE!"
        else:
            x=True

    return render(request, "recuperarpasswd2.html",{'form':form,'x':x, 'mensaje':mensaje})


def agregamascota(request):

    mascotas=Mascota.objects.all()
    if request.method == 'POST':
        form=UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()            
            return render(request, "listarmascota.html", {'mascotas':mascotas, 'mascotacreada':True})
    else:
        form = UploadImageForm()
    return render(request, "agregamascota.html", {'mascotas':mascotas, 'form':form})

@login_required(login_url='ingresar')
def servicios(request):
    personas=Persona.objects.all()
    mascotas=Mascota.objects.all()
    plantilla=loader.get_template("servicios.html")
    contexto={
        'mascotas':mascotas,
        'personas':personas
    }
    return HttpResponse(plantilla.render(contexto,request))

def ingresar(request):
    form=Login(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("codigoPersona"),password=data.get("password"))
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request,"ingresar.html",{'form':form})

def salir(request):
    logout(request)
    return redirect("/")

@login_required(login_url='ingresar')
def listarmascota(request):
    if request.user.is_staff:
        mascotas=Mascota.objects.all()
    else:
        mascotas=Mascota.objects.filter(estadoMascota="Disponible")
    
    plantilla=loader.get_template("listarmascota.html")
    contexto={
        'mascotas':mascotas
    }
    if request.method == 'POST':

        if request.POST.get("btnBorra") is not None:
            a = request.POST.get("codigo")
            mascota = Mascota.objects.get(codigoMascota=a)
            mascota.delete()
            return render(request, "listarmascota.html", {'mascotas':mascotas, 'mascotaeliminada':True})
        if request.POST.get("btnModifica") is not None:
            a = request.POST.get("codigo")
            m = Mascota.objects.get(codigoMascota=a)
            form = AgregarMascota(initial={'codigoMascota': m.codigoMascota, 'foto': m.foto, 'nombreMascota': m.nombreMascota, 'raza': m.raza, 'descripcion': m.descripcion, 'estadoMascota': m.estadoMascota, 'Persona': m.Persona})
            return render(request, "modificamascota.html", {'form':form, 'id':a})
        if request.POST.get("modificar") is not None:
            form=AgregarMascota(request.POST, request.FILES)
            mascota=Mascota.objects.filter(codigoMascota=request.POST.get("id"))
           
            ########################### FALTA ACTUALIZAR IMAGEN
            mascota.update(estadoMascota=request.POST.get("estadoMascota"), descripcion=request.POST.get("descripcion"), nombreMascota=request.POST.get("nombreMascota"), raza=request.POST.get("raza"))
            return render(request, "listarmascota.html", {'mascotas':mascotas, 'mascotamodificada':True})
    
    
    return HttpResponse(plantilla.render(contexto,request))

def galeria(request):
    mascotas=Mascota.objects.all()
    return render(request,"galeria.html",{'mascotas':mascotas})