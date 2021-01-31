from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from insta.forms import Trial

def index(request):
    context = {
        'form': Trial()
    }
    return render(request, 'insta/index.html', context)

def signin(request):
    return render(request, 'insta/signin.html')

def sesssion(request):
    input_username = request.POST['username']
    input_password = request.POST['password']
    user = authenticate(request, username=input_username, password=input_password)

    if user:
        login(request, user)
        return HttpResponseRedirect(reverse('home', args=(user.id,)))

    return HttpResponseRedirect(reverse('signin'))

@login_required
def home(request, user_id):
    return render(request, 'insta/home.html', {
        'user': request.user,
    })