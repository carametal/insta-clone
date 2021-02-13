from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('session/', views.session, name='session'),
    path('session_signup/', views.session_signup, name='session_signup'),
    path('post/', views.post, name='post'),
]
