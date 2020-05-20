from django.urls import path

from . import views

urlpatterns = [
    # path('', views.signIn, name='index'),
    path('receive', views.receive, name='receive'),
    path('connect', views.connect, name='connect'),
    path('bike_status', views.bike_status, name='bike_status'),
    path('android_status', views.android_status, name='android_status')
   ]