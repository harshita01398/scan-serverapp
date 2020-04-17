from django.urls import path

from . import views

urlpatterns = [
    # path('', views.signIn, name='index'),
    path('demo', views.demo, name='demo')
   ]