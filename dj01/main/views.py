from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# На главную страницу
def index(request):
    return HttpResponse("<h1> Это мой первый проект на Django </>")

# На другую страницу
def new(request):
    return HttpResponse("<h1> Это вторая страница моего проекта на Django </>")