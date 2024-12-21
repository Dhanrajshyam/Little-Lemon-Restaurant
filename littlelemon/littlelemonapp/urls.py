from django.urls import path
from . import views

app_name = 'littlelemonaapp'

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('contactus/', views.ContactusView.as_view(), name = 'contactus'),
    path('contactus/success/', views.contactedcustomeradded, name = 'contactsuccess'),
]