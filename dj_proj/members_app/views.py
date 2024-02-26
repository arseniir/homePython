from django.shortcuts import render
from .utils import process_request_session, create_form

'''Sorry for names in functions..'''

def input_page_view(request):
    process_request_session(request=request)
    return render(request, 'members.html', {'form': create_form()})


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
