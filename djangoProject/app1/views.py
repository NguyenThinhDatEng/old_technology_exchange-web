from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello world ")

def view1(request):
    return HttpResponse("<h1>Xin chao</h1><p> Hello</p>")