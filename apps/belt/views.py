# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.messages import error,success
from django.contrib import messages
import bcrypt
from django.shortcuts import render,redirect
from .models import *

# Create your views here.


def index(request):
    if 'id' not in request.session:
        return render(request, 'belt/index.html')
    else:
        context={
        'unique':User.objects.get(id=request.session['id']),
        'quotes':Quote.objects.exclude(favorite_Quote=request.session['id']),
        'faves':Quote.objects.filter(favorite_Quote=request.session['id'])
        }
        return render(request,'belt/success.html',context)


def create(request):
    errors=User.objects.validate(request.POST)
    if len(errors):
        for err in errors:
            error(request,err)
        return redirect('/')
    else:
        hashed = bcrypt.hashpw((request.POST['pass'].encode()), bcrypt.gensalt(5))
        User.objects.create(name=request.POST['name'],
        alias=request.POST['alias'],email=request.POST['email'],
        password=hashed,birth=request.POST['birth'])
        messages.success(request,'Shit has been added')
        return redirect('/')

def login(request):
    errors=User.objects.login(request.POST)
    if len(errors):
        for err in errors:
            error(request,err)
        return redirect('/')
    else:
        check=User.objects.filter(email=request.POST['lemail'])
        if len(check)>0:
            Users=check[0]
            if not bcrypt.checkpw(request.POST['lpass'].encode(), Users.password.encode()):
                messages.error(request,"Password or Login Are INCORRECT!")
                return redirect('/')
            request.session['id']=Users.id
            print User.objects.all()
            context={
            'person':User.objects.all(),
            'unique':User.objects.get(id=request.session['id'])
            }
            return redirect('/')
        else:
            messages.error(request,'Password or Login is wrong as FUCK!')
            return redirect('/')

def create_quote(request):
    errors=Quote.objects.quote(request.POST)
    if len(errors):
        for err in errors:
            error(request,err)
        return redirect('/')
    else:
        Quote.objects.create(author=request.POST['quoter'],
        quote=request.POST['message'],
        poster=User.objects.get(id=request.session['id']))
        messages.success(request,'Quote added has been added')
        return redirect ('/')

def logout(request):
    request.session.clear()
    return redirect('/')
def remove(request,number):
    a=Quote.objects.filter(favorite_Quote=number)
    a.delete()

    return redirect('/')

def user(request,number):
    context={
    'person':User.objects.get(id=number),
    'quotes':Quote.objects.filter(poster=User.objects.get(id=request.session['id'])),
    'count':Quote.objects.filter(poster=User.objects.get(id=request.session['id'])).count()
    }
    return render(request,'belt/user.html',context)
def add(request,number):
    a=User.objects.filter(id=request.session['id'])[0]
    b=Quote.objects.filter(id=number)[0]
    b.favorite_Quote.add(a)
    return redirect('/')
