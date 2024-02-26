from django.shortcuts import redirect, render
from .form import MyForm


def process_request_session(request): 
    if request.method == 'POST':
        form = create_form(request_data=request.POST)
        if form.is_valid():
            request.session['members_app'] = form.cleaned_data
            redirect('random_page')


            
def create_form(request_data=None):
    if request_data:
        return MyForm(request_data)
    
    return MyForm()



