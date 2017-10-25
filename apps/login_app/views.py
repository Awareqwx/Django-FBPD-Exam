# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt
from datetime import datetime

# Create your views here.
def index(request):
    if request.session.get("userid", False):
        return redirect("/friends/")
    return render(request, "loginApp/index.html")

def register(request):
    if request.session.get("userid", False):
        return redirect("/friends/")
    errors = User.objects.registerValidate(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect("/main/")  
    else:
        try:
            User.objects.get(email=request.POST["email"])
        except:
            request.session["userid"] = User.objects.create(
                name = request.POST["name"],
                alias = request.POST["alias"],
                email = request.POST["email"],
                password_hash = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()),
                birthday = datetime.strptime(request.POST["birthday"], '%Y-%m-%d')
            ).id
        else:
            messages.error(request, "Email already in use")
            return redirect("/signin/register/")
        return redirect("/friends/")

def login(request):
    errors = User.objects.loginValidate(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect("/main/")
    else:
        try:
            User.objects.get(email=request.POST["email"])
        except:
            messages.error(request, "Invalid email or password!")
            return redirect("/main/")
        else:
            if bcrypt.checkpw(request.POST["password"].encode(), User.objects.get(email=request.POST["email"]).password_hash.encode()):
                request.session["userid"] = User.objects.get(email=request.POST["email"]).id
                return redirect("/friends/")
            else:
                messages.error(request, "Invalid email or password!")
                return redirect("/main/")

def signout(request):
    if request.session.get("userid", False):
        request.session.flush()
        return render(request, "loginApp/signout.html")
    else:
        return redirect("/main/")