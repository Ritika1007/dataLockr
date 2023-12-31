from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
import sweetify

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # messages.success(request, "Registration Successful.")
            sweetify.success(request, 'Registration Successful.')
            return redirect('/')
        # messages.error(request, "Unsuccessful registration. Invalid information.")
        sweetify.error(request, 'Unsuccessful registration. Invalid information.')
    form = NewUserForm()
    return render (request=request, template_name="registration/register.html", context={"register_form":form})


def login_request(request):
    if request.method== 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password =  form.cleaned_data.get('password')
            user = authenticate(username=username, password = password)
            if user is not None:
                login(request, user)
                # messages.info(request, f"You are now logged in as {username}.")
                sweetify.success(request, 'Logged in Successfully!')
                return redirect("/")
            else:
                # messages.error(request,"Invalid username or password.")
                sweetify.error(request, 'Invalid login credentials.')
        else:
            # messages.error(request,"Invalid username or password.")
            sweetify.error(request, 'Invalid login credentials.')
    
    form = AuthenticationForm()
    return render (request=request, template_name="registration/login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    # messages.info(request, "Logged out successfully!")
    sweetify.success(request, 'Logged Out Successfully!')
    return redirect('/login')