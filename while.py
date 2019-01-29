#!/usr/bin/env python3.5
# Logic exercise
# Initiate by HarysMatta - tifosilinux.wordpress.com

import os
import py_compile


os.chdir("/home/hary/Documents/python/")
py_compile.compile('/home/hary/Documents/python/while.py')

##################################################################
##################################################################
#### FINAL RESULT
print()

class Logic:
    def pyramid(self):
        BOUNDARIES = 9
        A = 1
        while A <= BOUNDARIES:
            for Y in range(2, BOUNDARIES-1):
                print('+  ',end='')

            for B in range(A, 1, -1):
                print('%d ' % (A*B), end='')
            
            for D in range(1, A+1):
                print('%d ' % (A*D), end='')

            print()
            A+=1
            BOUNDARIES-=1

obj = Logic()
obj.pyramid()

print()
