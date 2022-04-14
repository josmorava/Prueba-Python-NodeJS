from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic
from .forms import ContentForm, LikesForm

from .models import Content


#Vistas genericas
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
  publication_list = Content.objects.order_by('-positive_votes')
  return render(request, "spa/index.html", {
    "publication_list" : publication_list
  })

def detail(request, element_id):
  """Detalle de cada elemento"""
  publication = get_object_or_404(Content, pk=element_id)
  
  if request.method=='POST':
    if 'like' in request.POST:
      publication.positive_votes +=1
      
    if 'dislike' in request.POST:
      publication.negative_votes +=1
    
  publication.save()
  
  return render(request, 'spa/detail.html',{
    "publication": publication,
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
  """Editar un elemento trayendo el id y apuntando ese id al formulario a editar(haciendo una instancia 'heredando')"""
  
  publication = get_object_or_404(Content, pk=element_id)
  form = ContentForm(request.POST or None, instance=publication)
  
  if form.is_valid() and request.method=='POST':
    form.save()
    return redirect('spa:content')
  
  return render(request, 'spa/edit.html',{
    'form': form
  })
    
def deleted(request, element_id):
  """Eliminar un elemento"""
  publication = get_object_or_404(Content , pk=element_id)
  publication.delete()
  return redirect('spa:content')

