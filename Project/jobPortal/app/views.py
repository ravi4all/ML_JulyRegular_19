from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(req):
#     return HttpResponse("<h1>Welcome to Job Portal</h1>")

def index(req):
    return render(req, 'index.html')

def register(req):
    return render(req, 'register.html')

def profile(req):
    return render(req, 'profile.html')