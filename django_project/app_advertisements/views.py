from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Успешно")


def test33(request):
    return HttpResponse("Test33")

