from django.urls import path
from .views import *

urlpatterns = [
    path('',Home.as_view(), name = 'home'),
    path('about/',About.as_view(),name = "about"),
    path('contact/',Contact.as_view(),"name=contact"),
    path('menu/',Menu_Viev.as_view(),name="menu")
    path('reservation/',Reservation.as_view(),name = reservation),
    path('servise/',Servise.as_view(),name="servise")
    path("testmonial/",Testmonial.as_view(),name ="

]
























