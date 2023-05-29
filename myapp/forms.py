from django import forms
from .models import Usuario

class UserForm(forms.ModelForm):
    password = forms.CharField(
        min_length=8,
        max_length=100,
        widget=forms.PasswordInput,
    )
    
    class Meta:
        model = Usuario
        exclude = (
                    'is_superuser', 'is_staff',
                    'is_active', 
                  )
        