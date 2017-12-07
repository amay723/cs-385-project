# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
#from django.template import loader

number = 1
player = 'X'
grid = []

def index(request):
    #template = loader.get_template('polls/index.html')

    global number
    number = 2

    global grid
    grid = [["." for i in range(3)] for j in range(3)]

    inner = [0, 1, 2]
    outer = [0, 1, 2]

    newgrid = []
    for i in range(0,3):
        for j in range(0,3):
            newgrid.append(grid[i][j])

    context = {
        'game_board': newgrid,
        'inner': inner,
        'outer': outer,
        'player': player
    }

    return render(request, 'polls/index.html', context)
    #return HttpResponse(template.render(context, request))
    #return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, sector_id):
    
    context = {
        'new_g': number
        }
    
    return render(request, 'polls/index.html', context)
    

def done(grid):

    if grid[0][1] == '0' and grid[0][0] == '0' and grid[0][2] == '0':
        return True
    elif grid[0][1] == 'X' and grid[0][0] == 'X' and grid[0][2] == 'X':
        return True
    # Top Row win cond

    elif grid[1][0] == '0' and grid[1][1] == '0' and grid[1][2] == '0':
        return True
    elif grid[1][0] == 'X' and grid[1][1] == 'X' and grid[1][2] == 'X':
        return True
    # Mid Row win cond

    elif grid[2][0] == '0' and grid[2][1] == '0' and grid[2][2] == '0':
        return True
    elif grid[2][0] == 'X' and grid[2][1] == 'X' and grid[2][2] == 'X':
        return True
    # Bottom Row win cond

    elif grid[0][1] == '0' and grid [1][1] == '0' and grid[2][1] == '0':
        return True
    elif grid[0][1] == 'X' and grid [1][1] == 'X' and grid[2][1] == 'X':
        return True
    # Mid down win cond

    elif grid[0][0] == '0' and grid[1][1] == '0' and grid[2][2] == '0':
        return True
    elif grid[0][0] == 'X' and grid[1][1] == 'X' and grid[2][2] == 'X':
        return True
    # Diagonal Right

    elif grid[2][0] == '0' and grid[1][1] == '0' and grid[0][2] == '0':
        return True
    elif grid[2][0] == 'X' and grid[1][1] == 'X' and grid[0][2] == 'X':
        return True
    # Diagonal Left

    elif grid[0][2] == '0' and grid[1][2] == '0' and grid[2][2] == '0':
        return True
    elif grid[0][2] == 'X' and grid[1][2] == 'X' and grid[2][2] == 'X':
        return True
    # Left Side Vertical

    elif grid[0][0] == '0' and grid[1][0] == '0' and grid[2][0] == '0':
        return True
    elif grid[0][0] == 'X' and grid[1][0] == 'X' and grid[2][0] == 'X':
        return True
    # Right Side Vertical

    else:
        return False


def move(request, sector_id):

    sector = sector_id

    global grid
    global player

    if player == "X":
        if sector == "1":
            grid[0][0] = 'X'
        elif sector == "2":
            grid[0][1] = 'X'
        elif sector == "3":
            grid[0][2] = 'X'
        elif sector == "4":
            grid[1][0] = 'X'
        elif sector == "5":
            grid[1][1] = 'X'
        elif sector == "6":
            grid[1][2] = 'X'
        elif sector == "7":
            grid[2][0] = 'X'
        elif sector == "8":
            grid[2][1] = 'X'
        elif sector == "9":
            grid[2][2] = "X"
        player = "O"
    elif player == "O":
        if sector == "1":
            grid[0][0] = 'O'
        elif sector == "2":
            grid[0][1] = 'O'
        elif sector == "3":
            grid[0][2] = 'O'
        elif sector == "4":
            grid[1][0] = 'O'
        elif sector == "5":
            grid[1][1] = 'O'
        elif sector == "6":
            grid[1][2] = 'O'
        elif sector == "7":
            grid[2][0] = 'O'
        elif sector == "8":
            grid[2][1] = 'O'
        elif sector == "9":
            grid[2][2] = "O"
        player = "X"
            
    
    inner = [0, 1, 2]
    outer = [0, 1, 2]

    newgrid = []
    for i in range(0,3):
        for j in range(0,3):
            newgrid.append(grid[i][j])

    context = {
        'game_board': newgrid,
        'inner': inner,
        'outer': outer,
        'lastSector': sector,
        'player': player
    }

    return render(request, 'polls/index.html', context)