from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .forms import AddContactedCustomerForm
# from os import path

# Create your views here.
def homepage(request):
    return HttpResponse('Home page for little Lemon Restuarant')

# APP_PATH = path.realpath(path.dirname(__file__))
# TEMPLATE_PATH = path.join(APP_PATH, 'templates/')
class ContactusView(CreateView):
    # model = ContactedCustomer
    form_class = AddContactedCustomerForm
    template_name = 'contactus.html'
    success_url = 'success/'

def contactedcustomeradded(request):
    return render(request, template_name='contactedcustomersuccess.html')
