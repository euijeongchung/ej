#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 16:56:10 2017

@author: ejchung
"""
introduction = "Please think of a number between 0 and 100!"
query_1 = "Is your secret number "
query_2 = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "
query_3 = "Sorry, I did not understand your input."
game_over = "Game over. Your secret number was: "
low = 0
high = 100
print(introduction)
while True:
    guess = int((low + high) / 2)
    print(query_1 + str(guess) + "?")
    answer = input(query_2)
    if (answer == "l"):
        low = guess
    elif (answer == "h"):
        high = guess
    elif (answer == "c"):
        break
    else:
        print(query_3)
print(game_over + str(guess))