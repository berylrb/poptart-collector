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
  path('poptarts/<int:poptart_id>/add_feeling/', views.add_feeling, name='add_feeling'),
  path('toppings/create/', views.ToppingCreate.as_view(), name='toppings_create'),
  path('toppings/<int:pk>/', views.ToppingDetail.as_view(), name='toppings_detail'),
  path('toppings/', views.ToppingList.as_view(), name='toppings_index'),
  path('toppings/<int:pk>/update/', views.ToppingUpdate.as_view(), name='toppings_update'),
  path('toppings/<int:pk>/delete/', views.ToppingDelete.as_view(), name='toppings_delete'),
]