# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 11:57:17 2017

Start the game: In the run time console type play()

Positions: 0-8 

Empty Cell: Defaults to 5

@author: rsharan

This game has imo a very high strategic importance in coding as it's arguments chess

"""
board=[[5,5,5],[5,5,5],[5,5,5]]

def displayboard():
    for i in range(0,3):
        print(board[i])

def inputP1():
    num1 = input('Enter position of X : ')
    return num1
def inputP2():
    num2 = input('Enter position of O : ')
    return num2

def play():
    k=1
    displayboard()
    while k<10:
        num3 =int(inputP1())
        i=int(num3/3)
        j= num3%3
        board[i][j]='X'
        k+=1
        displayboard()
        if (checkstatusWon()=='Won'):
            print('Won')
            break
        checkstatusDraw(k)
        num3 =int(inputP2())
        i=int(num3/3)
        j= num3%3
        board[i][j]='O'
        k+=1
        displayboard()
        if (checkstatusLoss()=='Lost'):
            print('Lost')
            break
    
    
def checkstatusWon():
    marker =0
    for i in range (0,3):
        if marker ==3 :
            return 'Won'
        else :
            marker =0
        for j in range(0,3):
            if board[i][j]=='X':
                marker +=1

def checkstatusLoss():
    marker =0
    for i in range (0,3):
        if marker ==3 :
            return 'Lost'
        else :
            marker =0
        for j in range(0,3):
            if board[i][j]=='O':
                marker +=1

def checkstatusDraw(k):
    if k==10:
        print('Draw')
