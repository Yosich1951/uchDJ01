from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# На главную страницу
def index(request):
    data = {'caption':"CatDjango"}
    return render(request, 'main/index.html', data)

# На другую страницу
def new(request):
    return render(request, 'main/new.html')

