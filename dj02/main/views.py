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

# На третью страницу
def new3(request):
    return render(request, 'main/third.html')

# На четвертую страницу
def new4(request):
    return render(request, 'main/fourth.html')

# На страницу О нас
def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')


