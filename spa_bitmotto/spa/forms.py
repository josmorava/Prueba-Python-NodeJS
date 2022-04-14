"""
  Formnulario para la creacion mediante un modelo de un elemento a mostrar
"""

from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import Content

class ContentForm(forms.ModelForm):
  class Meta:
    model = Content
    fields = [
      'title', 
      'content',
      'author',
    ]
    labels= {
      'title': ('Título del artículo'),
      'content': ('Contenido')
      ,'author': ('Autor del artículo')
    }
    
class LikesForm(forms.ModelForm):
  class Meta:
    model = Content
    fields = [
      'positive_votes',
      'negative_votes',
    ]