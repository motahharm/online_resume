from django.urls import path
from . import views

urlpatterns = [
  path('', views.index_view),
  path('resume/<id_user>', views.resume_view),
]