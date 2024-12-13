from django.shortcuts import render, redirect
from django.http import HttpResponse

def set_cookie(request):
    response = HttpResponse("Cookie is set")
    response.set_cookie('user_name', 'Your Name')  # Set a cookie
    return response

def set_session(request):
    request.session['user_email'] = 'your_email@example.com'  # Set a session variable
    return HttpResponse("Session is set")

def display_info(request):
    user_name = request.COOKIES.get('user_name', 'Guest')  # Retrieve cookie
    user_email = request.session.get('user_email', 'No email')  # Retrieve session variable
    return render(request, 'info.html', {'user_name': user_name, 'user_email': user_email})
