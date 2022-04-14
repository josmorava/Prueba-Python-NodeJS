from cProfile import label
from django.db import models

# Create your models here.

class Content(models.Model):
  """
  Modelo de la app principal del contenido a mostrar en el spa 
  """
  title = models.CharField(max_length=100)
  content = models.TextField(max_length=1000)
  author=models.CharField(max_length=30)
  date = models.DateField(auto_now_add=True)
  positive_votes=models.IntegerField(default=0)
  negative_votes=models.IntegerField(default=0)
  
  def __str__(self):
    return self.title