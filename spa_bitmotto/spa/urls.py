"""
Urls de la app spa
"""

from django.urls import path
from . import views

app_name = "spa"

urlpatterns = [
  path('', views.content, name="content"),
  path('create/', views.create, name="create"),
  path("edit/<int:element_id>",views.edit, name="edit"),
  path("deleted/<int:element_id>", views.deleted, name="deleted"),
  path("<int:element_id>/", views.detail,name="detail"),
]

