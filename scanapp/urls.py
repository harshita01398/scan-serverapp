from django.urls import path

from . import views

urlpatterns = [
    # path('', views.signIn, name='index'),
    path('receive', views.receive, name='receive'),
    path('connect', views.connect, name='connect'),
   ]