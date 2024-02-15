from django.shortcuts import render
from django.http import HttpResponse

def display_hello_world(request):
    return HttpResponse("Hello World")

def display_world(reuest):
    return HttpResponse("world")

def display_server(reuest):
    return HttpResponse("I am a Django server")