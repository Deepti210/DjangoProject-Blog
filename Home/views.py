from django.shortcuts import render
from django.http import HttpResponse

def home_page(reuest):
    return HttpResponse("Welcome to Home Page")

def signup_page(reuest):
    return HttpResponse("Are you a new user?. Sign-up Here")

def login_page(reuest):
    return HttpResponse("Already a Member! Just Log-In")
