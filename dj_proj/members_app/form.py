from django import forms

class MyForm(forms.Form):
    username = forms.CharField(label='Write your name:')
    age = forms.CharField(label='Write your age:')
    email = forms.EmailField(label='Write your email:')

