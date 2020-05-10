from django.urls import path

from . import views

urlpatterns = [
    # path('', views.signIn, name='index'),
    path('demo', views.demo, name='demo'),
    path('check_ip', views.check_ip, name='check_ip'),
    path('get_ip', views.get_ip, name='get_ip'),
    path('connect', views.connect, name='connect'),
   ]