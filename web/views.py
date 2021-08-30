from django.shortcuts import render
from . import models

def index_view(request):
  return render(request, 'index.html')

def resume_view(request, id_user):
  profile =  models.resume_model.objects.get(id=id_user)
  context = {'profile':profile}
  return render(request, 'resume.html', context)

def list_profile_view(request):
  profiles = models.resume_model.objects.all
  context = {'profiles':profiles}
  return render(request, 'list_profile.html', context)