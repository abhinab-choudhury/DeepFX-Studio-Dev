from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm


# Create your views here.
def index_view(request):
    return render(request, 'app/index.html')


def about_view(request):
    return render(request, 'app/about.html')


def service_view(request):
    return render(request, 'app/service.html')


def privacy_view(request):
    return render(request, 'app/privacy.html')


def terms_view(request):
    return render(request, 'app/terms-and-conditions.html')


@login_required
def dashboard_view(request):
    return render(request, 'app/dashboard.html')


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches with confirmation
        password = request.POST["password"]
        repeat_password = request.POST["confirm-password"]

        if password != repeat_password:
            messages.error(request, "Passwords do not match")
            return redirect('app:signup')
        else:
            pass
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)

            redirect('app:terms-and-conditions_view')
    else:
        form = UserRegistrationForm()

    return render(request, 'app/signup.html')


def signin(request):
    if request.method == 'POST':
        # required info
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username, password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, 'Invalid Credentials')
            redirect(request, 'app:sigin')
    else:
        pass
    return render(request, 'app/signin.html')


def signout(request):
    signout(request)
    return redirect('app:index_view')
