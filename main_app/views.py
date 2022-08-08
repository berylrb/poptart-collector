from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Poptart, Topping
from .forms import EmotionForm
from django.contrib.auth.views import LoginView

class Home(LoginView):
  template_name = 'home.html'

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

class PoptartCreate(LoginRequiredMixin, CreateView):
  model = Poptart
  fields = ['flavor', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class PoptartUpdate(UpdateView):
  model = Poptart
  fields = ['flavor', 'description']

class PoptartDelete(DeleteView):
  model = Poptart
  success_url = '/poptarts/'

class ToppingCreate(CreateView):
  model = Topping
  fields = '__all__'

def about(request):
  return render(request, 'about.html')

@login_required
def poptarts_index(request):
  poptarts = Poptart.objects.filter(user=request.user)
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


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('daddies_index')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)