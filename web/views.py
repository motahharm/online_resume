from django.shortcuts import render
from . import models

def index_view(request):
  return render(request, 'index.html')

def resume_view(request, id_user):
  profile =  models.resume_model.objects.get(id=id_user)
  context = {'profile':profile}
  return render(request, 'resume.html', context)