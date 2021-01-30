from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader
from insta.forms import Trial

def index(request):
    context = {
        'form': Trial()
    }
    return render(request, 'insta/index.html', context)

def signin(request):
    return render(request, 'insta/signin.html')