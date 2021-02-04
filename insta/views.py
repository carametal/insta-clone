from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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

def signup(request):
    return render(request, 'insta/signup.html')

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def session(request):
    input_username = request.POST['username']
    input_password = request.POST['password']
    user = authenticate(request, username=input_username, password=input_password)

    if user:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))

    messages.error(request, 'Incorrect username or password.')
    return HttpResponseRedirect(reverse('signin'))

def session_signup(request):
    try:
        input_password  = request.POST['password']
        input_confirm_password = request.POST['confirm_password']
        if input_password != input_confirm_password:
            messages.error(request, 'Not match password and confirm password.')
            return HttpResponseRedirect(reverse('signup'))
        
        username = request.POST['username']
        email = request.POST['email']
        User.objects.create_user(username, email, input_confirm_password)
        return HttpResponseRedirect(reverse('index'))
    except:
        messages.error(request, 'Username or email address is not available.')
        return HttpResponseRedirect(reverse('signup'))

