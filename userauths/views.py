from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from userauths.forms import UserRegistrationForm
from userauths.models import User

User = settings.AUTH_USER_MODEL

def RegisterView(request):
       
    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)   # request.POST to get entered values
        if form.is_valid():
            new_user= form.save()
            new_user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            login(request,new_user)
            return redirect("index")
    else:
        form = UserRegistrationForm   
    context ={
            "form":form,
        }
    return render(request,"userauths/sign-up.html", context)


def loginView(request):
    
    if request.method == "POST":
        email= request.POST.get("email")
        password = request.POST.get("password")
        
        user=authenticate(request,email=email,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,"You are logged in")
            return redirect("index")
        else:
            messages.warning(request,"Username or Password does not exist")
        
    return render(request,"userauths/sign-in.html")    
        
        
def logoutView(request):
    logout(request)
    return redirect("sign-in")        