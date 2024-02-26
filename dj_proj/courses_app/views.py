from django.shortcuts import render


def courses_send(request):
    '''this function outputs info if data in session'''
    data = request.session.get('members_app')
    print(f'Answer: {data}')
    message = "This is the course page" if data else  "You have no permissions"
    
    return render(request, 'courses.html', {'message': message})
    