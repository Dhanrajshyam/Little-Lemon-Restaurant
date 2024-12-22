from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin
from .models import ContactedCustomers


# Unregister the default UserAdmin 
admin.site.unregister(User)

# Create a new UserAdmin
@admin.register(User) 
class NewAdmin(UserAdmin): 
    readonly_fields = ['date_joined', 'last_login', ]

    def get_form(self, request, obj=None, **kwargs): 
        form = super().get_form(request, obj, **kwargs) 
        is_superuser = request.user.is_superuser 

        if not is_superuser: 
            form.base_fields['username'].disabled = True 

        return form
    


# Register your models here.
@admin.register(ContactedCustomers)
class ContactedCustomersAdmin(ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_email', 'customer_message', 'contacted_date', 'is_responded', 'responded_date')
