import os
import random
clear_output = lambda : os.system('clear')
stages = [
    '=====+=====',
    '     |',
    '     O',
    '    /|\ ',
    '    / \ '
]
chances = 5
random_words = ['tuple', 'dictionary', 'integer', 'float', 'string']
random_word = random.choice(random_words)
show_underlines = ['_ '] * len(random_word)

def ask_letter():
    letter = input('Enter your guess: ')
    while len(letter) != 1:
        letter = input('Enter one letter: ')
    return letter

def correct(letter):
    index = random_word.index(letter)
    show_underlines[index] = letter
    return ''.join(show_underlines)

def win(show_underlines):
    if '_ ' not in show_underlines:
        print('Congratulation! You have won..')
        game_on = False
        return game_on
    pass

print("Welcome to hangman \nAll the words are related to Pyton data objects.")

game_on = True
while game_on:
    
    print(''.join(show_underlines))
    letter = ask_letter()
    if letter in random_word:
        clear_output()
        for x in range(1, 6 - chances):
            print(stages[x-1])
        correct(letter)
          
    elif chances == 1:
        clear_output()
        for x in range(5):
            print(stages[x])
        print('you loose')
        break
    else:
        clear_output()
        chances -= 1
        for x in range(1, 6 - chances):
            print(stages[x-1])
        
    if '_ ' not in show_underlines:
        print('Congratulation! You have won..')
        break
