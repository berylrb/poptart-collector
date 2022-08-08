from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('poptarts/', views.poptarts_index, name='poptarts_index'),
  path('poptarts/<int:poptart_id>/', views.poptarts_detail, name='poptarts_detail'),
  path('poptarts/create/', views.PoptartCreate.as_view(), name='poptarts_create'),
  path('poptarts/<int:pk>/update/', views.PoptartUpdate.as_view(), name='poptarts_update'),
  path('poptarts/<int:pk>/delete/', views.PoptartDelete.as_view(), name='poptarts_delete'),
]