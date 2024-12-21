from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# from os import path

# Create your views here.
def homepage(request):
    return HttpResponse('Home page for little Lemon Restuarant')

# APP_PATH = path.realpath(path.dirname(__file__))
# TEMPLATE_PATH = path.join(APP_PATH, 'templates/')
class ContactusView(TemplateView):
    template_name = 'contactus.html'

