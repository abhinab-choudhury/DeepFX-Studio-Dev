from django.shortcuts import render

# Create your views here.


def signin_view(request):
    return render(request, 'authentication/signin.html')


def signup_view(request):
    return render(request, 'authentication/signup.html')
