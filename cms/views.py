from django.shortcuts import render
from django.http import HttpResponse
from models import Pages

# Create your views here.

def index(request, pagina):
	try:
		listado = Pages.objects.get(name=pagina)
	except Pages.DoesNotExist:
		return HttpResponse('Lo sentimos, esta pagina no ha sido almacenada.')
	respuesta = str(listado.page)
	return HttpResponse(respuesta)

def pagina(request, indice):
	try:
		listado = Pages.objects.get(id=int(indice))
	except Pages.DoesNotExist:
		return HttpResponse('Lo sentimos, esta pagina no ha sido almacenada.')
	respuesta = str(listado.page)
	return HttpResponse(respuesta)
