import random
import time
import sys


def animate():
    i=0
    while i<6:
        sys.stdout.write('\r-')
        time.sleep(0.5)
        sys.stdout.write('\r\\')
        time.sleep(0.5)
        sys.stdout.write('\r|')
        time.sleep(0.5)
        sys.stdout.write('\r/')
        time.sleep(0.5)
        i+=1
    sys.stdout.write('\rDone!     ')


print('~~~~~~~~~~~~~~~~~~~~ THE UNBELIEVABLE MIND READER ~~~~~~~~~~~~~~~~~~~')
print('')
print('')
print('select a number')
time.sleep(10)
print('assuming that u have selected a number')
time.sleep(3)
print('multiply it by two')
time.sleep(7)
print('is that done!!')
time.sleep(2)
print('great')

add=random.randint(1,10)
while add%2!=0:
    add=random.randint(1,10)
print('add', add ,'to it ')
time.sleep(8)
print('doing great in maths hmmm....')
print('divide the result by two')
time.sleep(10)
print('u r a maths genius dude....')
time.sleep(5)
print('subtract ur number from the result')
time.sleep(10)
add2=random.randint(1,15)
print('add',add2,'to your number')
print('the game is about to end')
time.sleep(2)
input('press any key to show your result')
x='7'
if x!=' ':

    print('analysing ur number   ')
    animate()
        
    print('\nu haved selected a great number ')
    time.sleep(2)
    print('')
    print('i will tell u the final result ')
    print('')
    print(add/2+add2)
    time.sleep(2)
    print('stop smiling ')
    print('')
    print('start praising me P-:')

input('press any key to exit')
if x!=' ' :
    exit()
