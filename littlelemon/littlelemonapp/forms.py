from django import forms
from .models import ContactedCustomers

# class ContactusCustomerinfoForm(forms.Form):
#     customer_name = forms.CharField(max_length= 100, required= True, label= 'Name', help_text= 'Name of the Customer or User')
#     customer_email = forms.EmailField(max_length= 254, required= True, label= 'Email',help_text= 'Email address of the Customer or User')
#     customer_message = forms.CharField(required= False, label= 'Message', help_text= 'Customer message to us for a specific contact request')


class AddContactedCustomerForm(forms.ModelForm):
    class Meta:
        model = ContactedCustomers
        fields = ['customer_name', 'customer_email', 'customer_message']
        labels = { 
            'customer_name': 'Your Name', 
            'customer_email': 'Your Email', 
            'customer_message': 'Message',
            }

        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'customer_email': forms.EmailInput(attrs={'class': 'form-control'}), 
            'customer_message': forms.Textarea(attrs={'class': 'form-control'}),
        }