# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from ..app_reglogin.models import User
from .models import Secret
from django.core.urlresolvers import reverse

# Create your views here.
def homepage(request):
    #User.objects.all().delete()
    context = {
                    'secretdata' :  Secret.objects.all(),
                    "name": request.session['first_name']                
                }
    print context
    return render(request,'post_app/homepage.html', context)

def addsecret(request):
    #Book.objects.all().delete()
    ##Author.objects.all().delete()
    #Review.objects.all().delete()
    if request.method == "POST":
        print request.POST
        context = {
                "name": request.session['first_name'],
                "id" :request.session['user_id'],
                 
                }
        print context
        result = Secret.objects.addsecret(request.POST,context)
        print  result['status']
        if not result['status']:
             
            for error in result['errors']:
                messages.error(request,error)
                print "here"
            return redirect(reverse('secrets:add_secret'))
        else: 
            messages.success(request,"Successful")
            return redirect(reverse('secrets:add_secret'))
            
    else:
            print "ENTERED GET"
            context = {
                    'secretdata' :  Secret.objects.all(),
                    "name": request.session['first_name']    
             }
    return render(request,'post_app/homepage.html',context )


def addlike(request,id):    
    context = {
                "secretid" :id,
                "userid" :request.session['user_id']
                }
    result = Secret.objects.addlike(context)
    if not result['status']:
            for error in result['errors']:
                messages.error(request,error)
                print "here"
            #return redirect(reverse('secrets:add_like',kwargs={'id': id}))
            return redirect(reverse('secrets:home_page'))
    else: 
            messages.success(request,"Successful")
            return redirect(reverse('secrets:home_page'))

def logout(request):
    request.session.clear()
    return redirect('users:my_index')