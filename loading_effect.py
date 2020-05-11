import time
import sys


def animate():
    i=0
    while i<4:
        sys.stdout.write('\r-')
        time.sleep(1)
        sys.stdout.write('\r\\')
        time.sleep(1)
        sys.stdout.write('\r|')
        time.sleep(1)
        sys.stdout.write('\r/')
        time.sleep(1)
        i+=1
    sys.stdout.write('\rDone!     ')

animate()
#long process here


