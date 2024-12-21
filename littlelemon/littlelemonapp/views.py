from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def homepage(request):
    return HttpResponse('Home page for little Lemon Restuarant')


class ContactusView(TemplateView):
    template_name = 'contactus.html'

    