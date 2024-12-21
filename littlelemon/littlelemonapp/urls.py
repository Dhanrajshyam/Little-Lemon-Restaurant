from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('contactus/', views.ContactusView.as_view(), name = 'contactus'),
]