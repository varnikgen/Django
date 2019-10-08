from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def posts_list(request):
    return HttpResponse('<h1>Hello blog</h1>')
