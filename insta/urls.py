from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('sesssion', views.sesssion, name='sesssion'),
    path('home/<int:user_id>', views.home, name='home')
]