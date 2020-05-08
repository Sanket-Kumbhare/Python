import os
import random

clear_output = lambda : os.system('clear')

def dice(n):
    clear_output()
    print('[-------]')
    print(f'| {n[0]} {n[1]} {n[2]} |')
    print(f'| {n[3]} {n[4]} {n[5]} |')
    print(f'| {n[6]} {n[7]} {n[8]} |')
    print('[-------]')

n = {1:[' ',' ',' ',' ',0,' ',' ',' ',' '], 2:[' ',0,' ',' ',' ',' ',' ',0,' '], 3:[' ',' ',' ',0,0,0,' ',' ',' '],
    4:[0,' ',0,' ',' ',' ',0,' ',0], 5:[0,' ',0,' ',0,' ',0,' ',0], 6:[0,0,0,' ',' ',' ',0,0,0]}


while True:

    y_or_n = input("\nPress 'y' roll again: ").lower()

    number = random.randint(1,6)

    if y_or_n == 'y':

        if number == 1:
            dice(n[1])

        elif number == 2:
            dice(n[2])

        elif number == 3:
            dice(n[3])

        elif number == 4:
            dice(n[4])

        elif number == 5:
            dice(n[5])

        else:
            dice(n[6])
        
    else:
        break
