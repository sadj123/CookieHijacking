from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import brow
from .models import Cookie
from django.contrib.auth import authenticate, login


@login_required
@brow()
def Home(request):
    return HttpResponse("Entre!")

def Login(request):
    if request.method=='POST':
        user=authenticate(username= request.POST.get("username"), password= request.POST.get("password"))
        if user is not None: 
            print("Entre")
            coo_f= Cookie.objects.get(user= user.id)
            coo_f.coo= request.META["HTTP_USER_AGENT"]
            coo_f.save()
            login(request, user)
            return redirect('/')
        else:
            print("Entre2")
            return redirect("/login")
    print("Entre3")
    return render(request, "login.html")
