from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader
from insta.forms import Trial

def index(request):
    template = loader.get_template('insta/index.html')
    context = {
        'form': Trial()
    }
    return HttpResponse(template.render(context, request))

def signin(request):
    return render(request, 'insta/signin.html')