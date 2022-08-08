from django.shortcuts import render

from django.http import HttpResponse
from .models import Poptart

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



# poptarts = [
#   Poptart('Strawberry', "A true classic. Kind of boring but also she's always there for you"),
#   Poptart('Brown Sugar Cinnamon', "Everyone's favorite and she knows it."),
#   Poptart('Wild Berry', "Strawberry's cooky cousin."),
#   Poptart('Hot Fudge Sundae', "A truly decadent choice for breakfast. Kind of a red flag honestly.")
# ]
