# -*- coding: utf-8 -*-
'''Views.py file for randomrouting app
by Troy Center June 2017, Coding Dojo'''
from __future__ import unicode_literals
from django.shortcuts import render
# Create your views here.
def home(request):
    '''render the home page with instructions'''
    return render(request, 'randomrouting/home.html')
def show(request, custnum):
    '''Render the landscapes page'''
    context = {}
    print request.method
    print request.session
    number = int(custnum)
    if number >= 1 and number <= 10:
        context = {
            "custfile": "snowlandscape.jpg"
        }
    elif number >= 11 and number <= 20:
        context = {
            "custfile": "desertlandscape.jpg"
        }
    elif number >= 21 and number <= 30:
        context = {
            "custfile": "forestlandscape.jpg"
        }
    elif number >= 31 and number <= 40:
        context = {
            "custfile": "vineyardlandscape.jpg"
        }
    elif number >= 41 and number <= 50:
        context = {
            "custfile": "tropicallandscape.jpg"
        }
    print "*"*50
    print "context: ", context
    print "*"*50
    return render(request, 'randomrouting/show.html', context)
