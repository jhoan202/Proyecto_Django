from django.shortcuts import render 

def principal(request):
	return render(request,'Principal.html')
def About_us(request):	
	return render(request,'About_us.html')
def handler_not_found(request,exception):
	return render(request,'Error_404.html')