from django import forms

class MyForm(forms.Form):
    username = forms.CharField(label='Write your username:')
    email = forms.EmailField(label='Write your email:')

