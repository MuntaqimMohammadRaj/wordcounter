
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeview, name='home'),
    path('count/',views.counter,name='count'),
    path('about/',views.about,name='about'),
]
