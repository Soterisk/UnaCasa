from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # or wherever you want to redirect after a successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'user/registration.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # form uses 'username' field for the USERNAME_FIELD
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)  # authenticate using email
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {email}.")
                return render(request, "home.html")
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid email or password.")
    form = AuthenticationForm()
    return render(request, "user/login.html", {"login_user": form})

def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")