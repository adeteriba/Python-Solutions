# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

#Within this function contain the list of words used in the game
def get_word():
    words = ['Adekunle']
    return random.choice(words).upper()
#We returned the function randomly using the random import at the top of the code in uppercase
    
def check(word,guess,guesses): #Fuction the check the word
    status = ''
    matches = 0
    #I am gonna loop through the letters in the word
    for letter in word:
        if letter in guesses:
            status = status + letter #Letter is added to the string
        else:
            status += '*' # * is added o the string to the user   
        if letter == guess:
            matches += 1
            #For every match we get we add on to matches
            
    if matches > 1:
        print('Yes! The word contains',matches,'"'+ guess + '"' + 's')
    elif matches == 1:
        print('Yes! The word contains',matches,'"'+ guess + '"')
    else:
        print('Hard luck! try again')
        
    return status #Return the word

def main():
    word = get_word()
    guesses = [] #Guesses is assigned a empty list
    guessed = False #Guessed is set to boolean false
    print('The word contains',len(word),'leters.')
    while not guessed:
        text = 'Please eneter one letter or a {} letter word. '.format(len(word)) #len(world) will replca eht e cyrly barcket entry
        guess = input(text)
        guess = guess.upper() #We can thereofre compare uppercase letters to upercase letters
        if guess in guesses:
            print('You already guessed "'  + guess + '"')
        elif len(guess) == len(word): #If the length of the guess equal the word
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print('Sorry, that is incorrect')
        elif len(guess) == 1:
                guesses.append(guess)
                result = check(word,guesses,guess)
                if result == word:
                    guessed == True
                else:
                    print(result)
        else:
            print('Invalid entry')
                     
    print('Yes, the word is',word + '! You got it in',len(guesses), 'tries')
        
main()
        



    
