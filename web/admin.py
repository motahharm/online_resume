from django.contrib import admin
from . import models

class resume_admin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'confirmed')
  list_display_links = ('first_name', 'last_name')
  list_editable = ['confirmed']

admin.site.register(models.resume_model, resume_admin)