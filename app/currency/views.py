from django.shortcuts import render
from django.http import HttpResponse

def my_first_app_django(request):
    return HttpResponse("Hello World!")
