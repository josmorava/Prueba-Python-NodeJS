from django.contrib import admin

from .models import Content


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
  list_display=(
    "title","date","positive_votes","negative_votes",
  )
  list_filter=["positive_votes"]
  search_fields= ["title"]
    
  