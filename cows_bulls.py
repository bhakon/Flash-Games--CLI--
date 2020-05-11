import time
from itertools import permutations
import random

def intro():
    print('welcome to the game ')
    print('')
    print('*************** The Game Of Intellectuals ***************')
    print('')
    
def select_no():
    lst=list(permutations('123456789',4))
    return ''.join(list(random.choice(lst)))
    

def game_start():
    time.sleep(2)
    print('generating number for YOU ... ')
    time.sleep(2)
    print('please wait.....')
    time.sleep(3)
    print('')
    print('number generated !!!')
    global num
    num=select_no()
    while num[0]=='0':
        num=select_no()

    
    num= int(num)
    play()

def play():
    chances=int(input('number of chances you want to guess the number : '))
    while chances!=1:
        print('')
        guess=int(input('guess the number :'))
        if len(str(guess))!=4:
            print('u lost ur chance because u entrerd a number other than 4 ')
            continue
        bulls=0
        cows=0
        for i in range(4):
            
            if str(guess)[i]==str(num)[i]:
                bulls+=1
            if str(guess)[i] in str(num) and str(guess)[i]!=str(num)[i]:
                cows+=1
        
        print('cows : ',cows)
        print('bulls : ',bulls)
        if bulls==4:
            won()

        chances-=1
            
        
    if bulls!=4:
        lose()
    else:
        won()


def won():
    print('u r a brilliant !!!! you won the game')
    another_game()

def lose():
    
    print('oof ohhh !! u lose the game ')
    print('-_- -_- -_-')
    print('by the way number is ' ,num)
    print('keep on doing u will get it one day')
    another_game()

def another_game():
    d=input('want to play another game [y/n]: ')
    if d=='y' or d=='Y' :
        game_start()

    else:
        exit()

intro()
game_start()
