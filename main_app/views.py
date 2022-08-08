from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Poptart, Topping
from .forms import EmotionForm

class ToppingList(ListView):
  model = Topping

class ToppingDetail(DetailView):
  model = Topping

class ToppingUpdate(UpdateView):
  model = Topping
  fields = ['name', 'color']

class ToppingDelete(DeleteView):
  model = Topping
  success_url = '/toppings/'

class PoptartCreate(CreateView):
  model = Poptart
  fields = ['flavor', 'description']


class PoptartUpdate(UpdateView):
  model = Poptart
  fields = ['flavor', 'description']

class PoptartDelete(DeleteView):
  model = Poptart
  success_url = '/poptarts/'

class ToppingCreate(CreateView):
  model = Topping
  fields = '__all__'

def home(request):
  return HttpResponse('<h1>Hi</h1>')

def about(request):
  return render(request, 'about.html')

def poptarts_index(request):
  poptarts = Poptart.objects.all()
  return render(request, 'poptarts/index.html', { 'poptarts': poptarts })

def poptarts_detail(request, poptart_id):
  poptart = Poptart.objects.get(id=poptart_id)
  toppings_poptart_doesnt_have = Topping.objects.exclude(id__in = poptart.toppings.all().values_list('id'))
  emotion_form = EmotionForm()
  return render(request, 'poptarts/detail.html', { 'poptart': poptart, 'emotion_form': emotion_form, 'toppings': toppings_poptart_doesnt_have })

def add_feeling(request, poptart_id):
  form = EmotionForm(request.POST)
  if form.is_valid():
    new_feeling = form.save(commit=False)
    new_feeling.poptart_id = poptart_id
    new_feeling.save()
  return redirect('poptarts_detail', poptart_id=poptart_id)

def assoc_topping(request, poptart_id, topping_id):
  Poptart.objects.get(id=poptart_id).toppings.add(topping_id)
  return redirect('poptarts_detail', poptart_id=poptart_id)