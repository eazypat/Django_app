from django import forms

class HumanForm(forms.Form):
    name = forms.CharField(required=True, label='Name', 
                    widget=forms.TextInput(attrs={'placeholder': 'Luis Obasanjo', 'class':'form-control'}))
    email = forms.EmailField(required=True, label='Email', 
                    widget=forms.TextInput(attrs={'placeholder': 'lObj@django.com', 'class':'form-control'}))