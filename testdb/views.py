from django.shortcuts import render
from django.http      import HttpResponse
from .models          import Teacher

# Create your views here.

def homepage(request):
  asaatza = Teacher.objects.all()
  print(asaatza)
  return render(request, 'testdb/homepage.html', {'asaatza' : asaatza})
