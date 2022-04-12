from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic
from .forms import ContentForm

from .models import Content

# Crea te your views here.

#class IndexView(generic.ListView):
  #"""
   # -Mostrar publicaciones
   #-Ordenar publicaciones por votos
  #"""
  #pass

#class DetailView(generic.DetailView):
  #"""
    #-Detalle de la pubvlicacion
    #-sistema de votacion
  #"""
  #pass

def content(request):
  """Mostrar todos los elementos ordenados por mayores votos positivos"""
  content_list = Content.objects.order_by('-positive_votes')
  return render(request, "spa/index.html", {
    "content_list" : content_list
  })

def detail(request, element_id):
  """Detalle de cada elemento"""
  element = get_object_or_404(Content, pk=element_id)
  return render(request, 'spa/detail.html',{
    "element": element
  })
  
def create(request):
  """Crear un nuevo elemento"""
  form = ContentForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('spa:content')
  return render(request, 'spa/create.html', {
    "form": form
  })

def edit(request, element_id):
  """Editar un elemento trayendo el id y apuntando ese id al formulario a editar (contentform)"""
  element = get_object_or_404(Content, pk=element_id)
  form = ContentForm(request.POST or None, instance=element)
  
  if form.is_valid() and request.method=='POST':
    form.save()
    return redirect('spa:content')
  
  return render(request, 'spa/edit.html',{
    'form': form
  })

def deleted(request, element_id):
  """Eliminar un elemento"""
  element = get_object_or_404(Content , pk=element_id)
  element.delete()
  return redirect('spa:content')

def prueba(request):
  return HttpResponse("Hola esta es una prueba")