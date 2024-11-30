from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile_pharma,Profile_cust
from itertools import chain
import random
# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def signin(request):
    return render(request,'signin.html')
    

@login_required(login_url='signin')    
def signout(request):
    auth.logout(request)
    return redirect('homepage')

def signup_p(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save

                #log user in and redirect to settings page
                user_login=auth.authenticate(username=username,password=password)
                auth.login(request,user_login)
                #create a profile model for the user
                user_model=User.objects.get(username=username)
                new_profile= Profile_pharma.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('setting')
        else:
            messages.info(request,'Password do not match')
            return redirect('signup')    
    else:
        return render(request,'signup.html')
    
def signup_c(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save

                #log user in and redirect to settings page
                user_login=auth.authenticate(username=username,password=password)
                auth.login(request,user_login)
                #create a profile model for the user
                user_model=User.objects.get(username=username)
                new_profile= Profile_cust .objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('setting')
        else:
            messages.info(request,'Password do not match')
            return redirect('signup')    
    else:
        return render(request,'signup.html')    