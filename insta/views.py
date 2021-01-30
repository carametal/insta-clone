from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from insta.forms import Trial

def index(request):
    context = {
        'form': Trial()
    }
    return render(request, 'insta/index.html', context)

def signin(request):
    return render(request, 'insta/signin.html')

def authentication(request):
    input_username = request.POST['username']
    input_password = request.POST['password']
    user = authenticate(username=input_username, password=input_password)
    if user:
        return HttpResponse("signed in.")
    else:
        return HttpResponse("invalid input.")
