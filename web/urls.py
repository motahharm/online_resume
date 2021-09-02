from django.urls import path
from . import views

urlpatterns = [
  path('', views.index_view, name='home'),
  path('profile/list/', views.list_profile_view, name='profile_list'),
  path('profile/create/', views.create_resume_view, name='resume_create'),
  path('profile/search/', views.search_resume_view, name='search_resume'),
  path('resume/<id_user>', views.resume_view, name='resume_view'),
]