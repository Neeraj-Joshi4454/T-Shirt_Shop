from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# ----------------customer authentication------------------

class CustomerAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(required=True, label="Email")



# -------------------customer signup--------------------
class CustomerCreationForm(UserCreationForm):
    username = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(required=True, label="First Name")
    last_name = forms.CharField(required=True, label="Last Name")

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        if len(value.strip()) < 3:
            raise ValidationError("First name should be greater than 3 characters....") 
        return value.strip()

        
    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        if len(value.strip()) < 3:
            raise ValidationError("last name should be greater than 3 characters....") 
        return value.strip()
    

    class Meta:
        model = User
        fields = ['username','first_name','last_name']