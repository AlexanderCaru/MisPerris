from django.db import models
from django.contrib.auth.models import User

estadoMascota=(
		('Rescatado','Rescatado'),
		('Disponible','Disponible'),
		('Adoptado','Adoptado')
	)
# Create your models here.
#userDefault=User.objects.get(username="defecto")
class Persona(models.Model):
    codigoPersona = models.CharField(max_length=10, primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE, null=True )
    nombrePersona = models.CharField(max_length=50)
    correoPersona=models.TextField(null=True)
    fechaNac=models.DateField(max_length=10,null=True)
    telefono=models.CharField(max_length=9,null=True)
    region=models.TextField(null=True)
    ciudad=models.TextField(null=True)
    tipoVivienda=models.TextField(null=True)
    def __str__(self):
       return self.nombrePersona+ " "+str(self.codigoPersona)

class Mascota(models.Model):
    codigoMascota = models.AutoField(primary_key=True)
    foto=models.ImageField(upload_to='Sistema/static/imagesmascotas/',null=True)
    nombreMascota = models.CharField(max_length=50,null=True)
    raza=models.CharField(max_length=50,null=True)
    descripcion=models.TextField(null=True)
    estadoMascota = models.CharField(max_length=50, choices=estadoMascota, default = "Rescatado",null=True)
    Persona = models.ForeignKey(Persona, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombreMascota+ " "+str(self.codigoMascota)+ " "+str(self.estadoMascota)+ " "+str(self.Persona)
