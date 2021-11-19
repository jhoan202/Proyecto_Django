from django.db import models

# Create your models here.
class Mi_modelo(models.Model):

	Nombre=models.CharField(max_length=20)
	Apellido=models.CharField(max_length=30)
	number_tarjeta=models.IntegerField()
	fecha_tarjeta=models.DateField(null=True)
	codigo_seguridad=models.IntegerField(null=True)
	usuario=models.CharField(max_length=30, null=False)
	contraseña=models.CharField(max_length=30, null=False)