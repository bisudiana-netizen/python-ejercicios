from django.shortcuts import render
from django.http import HttpResponse
from .models import Noticia

# Create your views here.

def index(request):

   return render(request, 'index.html')

def noticias(request):
   entradas = Noticia.objects.all()
   context = {'entradas': entradas}
   template = 'blog/home.html'
   return render(request, template, context)

def formulario(request):
   return render(request, 'blog/formulario.html')

def detalle_entrada(request, id):
   entrada = Noticia.objects.get(id=id)
   context = {'entrada': entrada}
   return render(request, 'blog/detalle_entrada.html', context)
    
