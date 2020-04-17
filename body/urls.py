from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),

    path('team/',views.team,name='body-team'),
    path('events/',views.events,name='body-events'),
    path('contact/',views.contact,name='contact'),
    path('gallery/',views.gallery,name='gallery'),
    path('index/',views.index,name='body-index'),


    ]
