from django.shortcuts import render, redirect
from . import models

def index_view(request):
  return render(request, 'index.html')

def resume_view(request, id_user):
  profile =  models.resume_model.objects.get(id=id_user)
  context = {'profile':profile}
  return render(request, 'resume.html', context)

def list_profile_view(request):
  profiles = models.resume_model.objects.all()[0:5]
  context = {'profiles':profiles}
  return render(request, 'list_profile.html', context)

def create_resume_view(request):
  from .forms import resume_create_form
  if request.method == "POST":
    resume_form = resume_create_form(request.POST)
    if resume_form.is_valid() :
      first_name = resume_form.cleaned_data['first_name']
      last_name = resume_form.cleaned_data['last_name']
      description = resume_form.cleaned_data['description']
      new_resume = models.resume_model(first_name = first_name, last_name = last_name, description = description)
      new_resume.save()
      return redirect('/')

  context = {'resume_create_form': resume_create_form}
  return render(request, 'create_resume.html', context)

def search_resume_view(request):
  if request.method == "POST":
    if request.POST['search'] is not None:

      resumes = models.resume_model.objects.extra(
        where=[f"first_name LIKE '%{request.POST['search']}%' OR last_name LIKE '%{request.POST['search']}%'"]
      )

      context = {'resumes':resumes}
      return render(request ,'search_resume.html', context)
  
  return render(request ,'search_resume.html')