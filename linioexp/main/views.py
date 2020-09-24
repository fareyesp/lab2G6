from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from.models import *

def home(request):
  return HttpResponse("Hola Mundo. Te encuentras en la página de inicio del Linio Express")

class ProductListView(ListView):
  model = Producto

class ProductDetailView(DetailView):
  model = Producto

class ProveedorListView(ListView):
  model = Proveedor

class ProveedorDetailView(DetailView):
  model = Proveedor

class CategoriaListView(ListView):
  model = Categoria

class CategoriaDetailView(DetailView):
  model = Categoria

class LocalizacionListView(ListView):
  model = Localizacion

class LocalizacionDetailView(DetailView):
  model = Localizacion
