from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('poptarts/', views.poptarts_index, name='poptarts_index'),
  path('poptarts/<int:poptart_id>/', views.poptarts_detail, name='poptarts_detail'),
]