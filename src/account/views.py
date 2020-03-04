from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

from .forms import CreateUser

def accountList(request):
    user_count=User.objects.count()
    context= {
        'user_count': user_count,
    }
    return render(request , 'account/accountList.html', context)


def register(request):
    form = CreateUser()
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            user= form.cleaned_data.get('username')
            messages.success(request, 'Account was succesfully created for ' + user)
            return redirect('login_page')

    context={
        'form': form,
    }
    return render(request , 'account/register.html' ,context)


def loginPage(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username , password=password)
        if user is not None:
            login(request, user)
            return redirect('userAccount_page')
        else:
            messages.info(request,'Username or password is incorrect')

    context={

    }
    return render(request, 'account/login.html', context)


def userAccount(request):
    context ={

    }
    return render(request, 'account/userAccount.html' , context)
