from django.db import models

# Create your models here.
class ContactedCustomers(models.Model):
    id = models.AutoField(primary_key= True, verbose_name= 'ID', help_text= 'Unique reference for request from customer or user who wanted to contact us')
    customer_name = models.CharField(max_length= 254, blank= False, null= False, help_text='Customer name who requested to contact us')
    customer_email = models.EmailField(max_length= 254, blank= False, null= False, help_text= 'Customer email address')
    customer_message = models.TextField(blank= True)
    contacted_date = models.DateTimeField(auto_now= True, help_text= 'DataTime of the customer request to contact us')
    is_responded = models.BooleanField(default= False, help_text= 'It shows whether we responded back on the customer request')
    responded_date = models.DateTimeField(help_text= 'Date on which we responded back to the customer', blank= True, null= True)

    def __str__(self):
        return self.customer_name