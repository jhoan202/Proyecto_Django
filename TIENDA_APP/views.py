from django.shortcuts import render
from TIENDA_APP.models import Mi_modelo
# Create your views here.

def Sign_up(request):
	return render(request,'Sign_Up.html')

def Confirm_Identity(request):
	return render(request,'Confirmation.html')

def Registro(request):
	nombre=request.POST["nombre"]
	apellido=request.POST["apellido"]
	credit_card=request.POST["number_credit"]
	usuario=request.POST["user"]
	constraseña=request.POST["password"]

	Mi_modelo.objects.create(Nombre=nombre,Apellido=apellido,number_tarjeta=credit_card,usuario=usuario,contraseña=constraseña)
	return render(request,'Principal.html')

def Loguearse(request):
	print("====================")
	user=request.POST["user"]
	password=request.POST["pass"]
	obtener_datos=Mi_modelo.objects.filter(usuario=user,contraseña=password)
	
	if obtener_datos:
		return render(request,'Logueo.html',{"logueado":"Has ingresado"})
	else:
		return render(request,'Logueo.html',{"logueado":"No Has ingresado"})
