from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Poptart



class PoptartCreate(CreateView):
  model = Poptart
  fields = '__all__'

class PoptartUpdate(UpdateView):
  model = Poptart
  fields = ['flavor', 'description']

class PoptartDelete(DeleteView):
  model = Poptart
  success_url = '/poptarts/'

def home(request):
  return HttpResponse('<h1>Hi</h1>')

def about(request):
  return render(request, 'about.html')

def poptarts_index(request):
  poptarts = Poptart.objects.all()
  return render(request, 'poptarts/index.html', { 'poptarts': poptarts })

def poptarts_detail(request, poptart_id):
  poptart = Poptart.objects.get(id=poptart_id)
  return render(request, 'poptarts/detail.html', { 'poptart': poptart })


