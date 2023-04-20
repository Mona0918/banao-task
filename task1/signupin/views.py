from django.shortcuts import render,redirect
from .forms import UserTypeForm,RegisterForm
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import SignUpModel
from django.http import HttpResponse

def homepage(request):
    return render(request,"signupin.html")

def usertyperview(request):
    if request.method=='POST':
        form=UserTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('signupin:signup'))
    else:
        form=UserTypeForm()
    return render(request,"typeofusers.html",{'usertype_form':form})

def registerview(request):
    if request.method=='POST':
        form=RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('signupin:signin'))
    else:
        form=RegisterForm()
    return render(request,'signup.html',{'register_form':form})

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            print('yes')
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                name=user.get_username()
                url = reverse('signupin:welcome')
                print(url)
                return redirect(url)
    else:
        form=AuthenticationForm()
    return render(request,'signin.html',{'form':form,'name':name})


def homeview(request,name):
    data=SignUpModel.objects.get(username=name)
    return render(request,'welcome.html',{'data':data})


def logoutview(request):
    auth_logout(request)
    return redirect(reverse('signupin:usertype'))


