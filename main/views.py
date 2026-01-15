from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse("this is the home page, welcome")


def greeting(request):
    return HttpResponse("hello world")
