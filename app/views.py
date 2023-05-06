from django.shortcuts import render
from django.views.generic import TemplateView, Createview, LIstView
#create your views here

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Contact(TemplateView):
    template_name = "contct.html"

class Menu_View(ListView):
    template_name = "contact.view"
    fields = "__all__"

class Restervation(TemplateView):
    model = book_your_table
    template_name = "restervation.html"
    fields = "__all__"

    

class Service(TemplateView):
    template_name = "service.html"

class Testmonial(TemplateView):
    template_name = "Testmonial.html"































