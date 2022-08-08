from django.shortcuts import render


from django.http import HttpResponse


class Poptart:
  def __init__(self, flavor, description):
    self.flavor = flavor
    self.description = description

poptarts = [
  Poptart('Strawberry', "A true classic. Kind of boring but also she's always there for you"),
  Poptart('Brown Sugar Cinnamon', "Everyone's favorite and she knows it."),
  Poptart('Wild Berry', "Strawberry's cooky cousin."),
  Poptart('Hot Fudge Sundae', "A truly decadent choice for breakfast. Kind of a red flag honestly.")
]

def home(request):
  return HttpResponse('<h1>Hi</h1>')

def about(request):
  return render(request, 'about.html')

def poptarts_index(request):
  return render(request, 'poptarts/index.html', { 'poptarts': poptarts })