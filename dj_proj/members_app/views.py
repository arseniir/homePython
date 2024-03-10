from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from .form import MyForm
from .utils import create_form
from .models import UserEnrollment, User



'''Sorry for names in functions..'''

class inputFormMembers(View):
    template_name='members.html'

    def get(self, request):
        return render(request, self.template_name, {'form': create_form()})

    def post(self, request):
        form = create_form(request_data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            errors = {}

        # Перевіряємо, чи є введені email або username
            if not username:
                errors['username'] = 'Please write username'
            if not email:
                errors['email'] = 'Please write email'

            if not errors:
            # Якщо обидва поля введені, шукаємо користувача за email та username
                user = User.objects.filter(email=email, username=username).first()
                if not user:
                    errors['user'] = 'User does not exist'
                else:
                # Якщо користувач знайдений, робимо енролл
                    usCreMem, created = UserEnrollment.objects.get_or_create(user=user)
                    usCreMem.email = email
                    usCreMem.save()

        return render(request, self.template_name, {'errors': errors, 'form': create_form()})









    # def post(self, request):
    #     form = create_form(request_data=request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         email = form.cleaned_data.get('email')
    #         user = User.objects.filter(email=email, username=username).first()
    #         errors = {}
    #         if not user:
    #             errors['user'] = 'User does not exist'
    #         if not email:
    #             errors['email'] = 'Please write email'

    #         if not errors:
    #             usCreMem, created = UserEnrollment.objects.get_or_create(user=user)
    #             usCreMem.email=email
    #             usCreMem.save()

    #         return render(request, self.template_name, {'errors': errors, 'form': create_form()})






def plusMinusWay(request):
    '''this function send info about email length '''
    data = request.session.get('members_app')
    print(f'Answerto: {data}')
    if len(data['email']) > 35:
        computer_text = "You have very long email"
    elif len(data['email']) > 15:
        computer_text = "You have good email length"
    else:
        computer_text = "Badly, you have very short email"
    return render(request, 'random_page.html', {'computer_text': computer_text})
