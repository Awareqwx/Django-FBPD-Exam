# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import User

# Create your views here.
def index(request):
    if not request.session.get("userid", False):
        return redirect("/main/")
    context = {
        "user":User.objects.get(id=request.session["userid"]),
        "notfriends":User.objects.exclude(friends=request.session["userid"]).exclude(id=request.session["userid"])
    }
    return render(request, "friendsApp/index.html", context)

def show(request, id): 
    # Intentionally not doing a signin check since there's no reason for
    # someone who isn't logged in to not be able to view a profile
    try:
        context = {
            "user":User.objects.get(id=id)
        }
    except:
        return redirect("/user/error/")
    return render(request, "friendsApp/show.html", context)

def add(request, id):
    if not request.session.get("userid", False):
        return redirect("/main/")
    user = User.objects.get(id=request.session["userid"])
    try:
        friend = User.objects.get(id=id)
    except:
        return redirect("/friends/error/")
    user.friends.add(friend)
    user.save()
    friend.friends.add(user)
    friend.save()
    return redirect("/friends/")

def remove(request, id):
    if not request.session.get("userid", False):
        return redirect("/main/")
    user = User.objects.get(id=request.session["userid"])
    try:
        friend = User.objects.get(id=id)
    except:
        return redirect("/friends/error/")
    user.friends.remove(friend)
    user.save()
    friend.friends.remove(user)
    friend.save()
    return redirect("/friends/")

def error(request):
    return render(request, "friendsApp/error.html")