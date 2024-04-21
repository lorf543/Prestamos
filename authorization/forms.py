from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=False)
    
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            
    class Meta:
        model= User
        labels ={

        }
        
        fields = ["username", "password1", "password2"]
        exclude = ["email",]
        
        widgets = {
            'username': forms.TextInput (
                attrs={
                    'hx-post':'/check-username/',
                    'hx-swap':'outerhtml',
                    'hx-triger':'keyup delay:2s',
                    'hx-target':'#username_error'
                }
            )
        }
