from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# На главную страницу
def index(request):
    return HttpResponse("<h1> Это мой первый проект на Django </>")

# На другую страницу
def new(request):
    return HttpResponse("<h1> Это вторая страница моего проекта на Django </>")

# На страницу data
def data(request):
    return HttpResponse("<h1> Это страница data моего проекта на Django </>")

# На страницу test
def test(request):
    return HttpResponse("<h1> Это страница test моего проекта на Django </>")
