# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
#from django.template import loader

number = 1

def index(request):
    #template = loader.get_template('polls/index.html')

    global number
    number = 2

    grid = [["." for i in range(3)] for j in range(3)]

    i = [0, 1, 2]
    j = [0, 1, 2]
    context = {
        'game_board': grid,
        'outer': i,
        'inner': j
    }

    return render(request, 'polls/index.html', context)
    #return HttpResponse(template.render(context, request))
    #return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, sector_id):
    
    context = {
        'new_g': number
        }
    
    return render(request, 'polls/index.html', context)
    
