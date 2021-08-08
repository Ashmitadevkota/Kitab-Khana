from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import forms
from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import UserCreation,LoginForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your views here.
def registerFunction(request):
    if request.method =="POST":
            form = UserCreation(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Account is created successfully!")
                return HttpResponseRedirect('')
            else:
                log = LoginForm(request = request,data = request.POST)

    else:  
        forms = UserCreation()
    return render(request,"html/auth/register.html",{'form':form})

def loginFunction(request):
    if request.method == 'POST':
        form = LoginForm(request = request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pas = form.cleaned_data['password']
            usr = authenticate(username=username,password = pas)
            login(request,usr)
            return HttpResponse("Login success")
    else:
        log = LoginForm()
    return render(request,"html/auth/login.html",{'form':form})

