from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='body-index'),

    path('team/',views.team,name='body-team'),
    path('events/',views.events,name='body-events'),
    path('contact/',views.contact,name='contact'),
    path('gallery/',views.gallery,name='gallery'),


    ]
