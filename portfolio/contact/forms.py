from django import forms 
from .models import contact


class Contact_Form(forms.Form):
    name = forms.CharField(max_length =100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(help_text = 'null@mail.com', widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(max_length = 300, widget=forms.TextInput(attrs={'class':'form-control'}))
