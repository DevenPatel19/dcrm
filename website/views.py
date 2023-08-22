from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def home(request):
    # Check to see if logging in
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully Logged in!.')

            return redirect('home')

        else:
            messages.success(request, 'There was an error logging in.')

            return redirect('home')
    else:

        return render(request, "home.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out")
    return redirect('home')
