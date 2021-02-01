from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from insta.forms import Trial

def index(request):
    context = {
        'form': Trial(),
        'user': request.user,
        'username': request.user.username
    }
    return render(request, 'insta/index.html', context)

def signin(request):
    return render(request, 'insta/signin.html')

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def sesssion(request):
    input_username = request.POST['username']
    input_password = request.POST['password']
    user = authenticate(request, username=input_username, password=input_password)

    if user:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))

    return HttpResponseRedirect(reverse('signin'))
