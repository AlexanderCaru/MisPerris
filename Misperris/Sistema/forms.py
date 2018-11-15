from django import forms
from .models import Mascota
from datetime import datetime
region=(
		('--Región--','--Región--'),
		('Arica y Parinacota','Arica y Parinacota'),
		('Coquimbo','Coquimbo'),
		('Metropolitana','Metropolitana')
	)
ciudad=(
		('--Ciudad--','--Ciudad--'),
	)
tipovivienda=(
		('--Tipo--','--Tipo--'),
		('Casa con patio grande','Casa con patio grande'),
		('Casa con patio pequeño','Casa con patio pequeño'),
		('Casa sin patio','Casa sin patio'),
		('Departamento','Departamento')
	)
tipoUsuario=(
		('Adoptante','Adoptante'),
		('Administrador','Administrador')
	)

estadoMascota=(
		('Rescatado','Rescatado'),
		('Disponible','Disponible'),
		('Adoptado','Adoptado')
	)

class AgregarPersona(forms.Form):
    codigoPersona=forms.CharField(widget=forms.TextInput(), label="RUN de persona")
    nombrePersona=forms.CharField(widget=forms.TextInput(), label="Nombre de persona")
    passwd=forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    passwd2=forms.CharField(widget=forms.PasswordInput(), label="Escriba contraseña nuevamente")
    correoPersona=forms.CharField(widget=forms.TextInput(), label="Correo")
    fechaNac=forms.DateField(widget=forms.SelectDateWidget(years=range(1900,datetime.now().year)), label="Fecha de Nacimiento")
    telefono=forms.CharField(widget=forms.TextInput(), label="Telefono")
    region=forms.ChoiceField(choices=region, label="Region")
    ciudad=forms.ChoiceField(choices=ciudad, label="Ciudad")
    tipoVivienda=forms.ChoiceField(choices=tipovivienda, label="Tipo Vivienda")
    esAdmin=forms.CharField(widget=forms.RadioSelect(choices=tipoUsuario), label="Tipo Usuario")

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields=['foto','nombreMascota','raza','descripcion','estadoMascota']


class RecuperarPasswd(forms.Form):
	codigoPersona=forms.CharField(widget=forms.TextInput(), label="RUN de persona")

class RetypePasswd(forms.Form):
	passwd=forms.CharField(widget=forms.TextInput(), label="Contraseña")
	passwd2=forms.CharField(widget=forms.TextInput(), label="Reescribir Contraseña")

class Login(forms.Form):
    codigoPersona=forms.CharField(widget=forms.TextInput(),label="RUN de persona")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")

class AgregarMascota(forms.Form):
    
    nombreMascota=forms.CharField(widget=forms.TextInput(),label="Nombre de mascota")
    raza=forms.CharField(widget=forms.TextInput(),label="Raza de mascota")
    descripcion=forms.CharField(widget=forms.TextInput(),label="Descripcion")
    estadoMascota = forms.ChoiceField(choices=estadoMascota,label="Estado Mascota")
