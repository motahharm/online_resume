from django.urls import path
from . import views

urlpatterns = [
  path('', views.index_view, name='home'),
  path('profile/list/', views.list_profile_view, name='profile_list'),
  path('resume/<id_user>', views.resume_view),
]