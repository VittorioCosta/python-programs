# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 20:02:36 2020

@author: slelenia
"""


def main():
    tab = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
        ]
    win = False
    player1(tab)
    player2(tab)
    while win==False and " " not in tab:
        player1(tab)
        s = "X"
        win = ceckWin(tab,s)
        if win is True: print("PLAYER 2 YOU WIN")
        if " " not in tab: ("END GAME")
        if win is False and " " not in tab:
            player2(tab)
            s = "0"
            win = ceckWin(tab,s)
            if win is True: print("PLAYER 2 YOU WIN")
            if " " not in tab: ("END GAME")
    return 
        
    
    
    


def player1(tab):
    for i in tab: print(i)
    print("\n")
    print("Player1")
    row = int(input("ROW---> "))
    column = int(input("COLUMN---> "))
    while tab[row][column]!=" ":
        row = int(input("ROW---> "))
        column = int(input("COLUMN---> "))
    tab[row][column]="X"
    return tab
    
def player2(tab):
    for i in tab: print(i)
    print("\n")
    print("Player2")
    row = int(input("ROW---> "))
    column = int(input("COLUMN---> "))
    while tab[row][column]!=" ":
        row = int(input("ROW---> "))
        column = int(input("COLUMN---> "))
    tab[row][column]="0"
    return tab

def ceckWin(tab,s):
    win = False
    if tab[0][0]==s and tab[0][1]==s and tab[0][2]==s: win = not win
    elif tab[1][0]==s and tab[1][1]==s and tab[2][1]==s: win = not win
    elif tab[2][0]==s and tab[2][1]==s and tab[2][2]==s:win = not win
    elif tab[0][0]==s and tab[1][0]==s and tab[2][0]==s:win = not win
    elif tab[0][1]==s and tab[1][1]==s and tab[2][1]==s:win = not win
    elif tab[0][2]==s and tab[1][2]==s and tab[2][2]==s:win = not win
    elif tab[0][0]==s and tab[1][1]==s and tab[2][2]==s:win = not win
    elif tab[0][2]==s and tab[1][1]==s and tab[2][0]==s:win = not win
    return win