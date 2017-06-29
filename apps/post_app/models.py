# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..app_reglogin.models import User
from django.db import models
import bcrypt

 

class secretManager(models.Manager):
    def addsecret(request,postData,sessiondata):
        print postData
        print " In addsecret %%%%%%%%%%%"
        
        results = {'status': True, 'errors': []}
        if not postData['secretinput'] or len(postData['secretinput'])<1:
            print "In validation1 "
            results['status'] = False
            results['errors'].append("Please enter a Secret")

        if results['status']:
            user1 = User.objects.get(id = sessiondata['id'])
            print "Successfully done@@@@@@@@@@@@@@"
            
            secret1 = Secret.objects.create(secretcontent=postData['secretinput'],secretuser = user1)
             
            print secret1
          
            results['status'] = True
            print "Successfully done!!!!!!!!!"
       
        return results            

    def addlike(request,context):
        print context
        results = {'status': True, 'errors': []}

        secret1=Secret.objects.get(id=context["secretid"])
        user1=User.objects.get(id=context["userid"])
        if secret1.secretuser == user1:
            print "In validation1 "
            results['status'] = False
            results['errors'].append("User cannot like his/her own secret")
        else:
            secret1.likers.add(user1)
            print "Like done!!!!!!!!!"
            results['status'] = True
        return results 
 


class Secret(models.Model):
    secretcontent = models.TextField(max_length=1000)
    secretuser = models.ForeignKey('app_reglogin.User', related_name="secretusers")
    likers = models.ManyToManyField('app_reglogin.User', related_name="secretlikers")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=secretManager()
    #bookauthors
    #bookreviews
 
 
    

