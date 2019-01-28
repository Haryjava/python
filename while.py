#!/usr/bin/env python3.5
# Logic exercise
# Iniriate by HarysMatta - tifosilinux.wordpress.com


BARU = 1
k = 5
while k >= BARU:
        l = 2
        while l <= k:
            print('+ ', end='')
            l += 1
        print() # new line
        k-=1
print()

##################################################################
##################################################################
#### FINAL RESULT

BOUNDARIES = 5
A = 2
while A <= BOUNDARIES:
    for B in range(A, 1, -1):
        print('%d ' % (A*B), end='')
    print()
    A+=1

print()

BOUNDARIES2 = 5
C = 1
while C <= BOUNDARIES2:
    for D in range(1, C+1):
        print('%d ' % (C*D), end='')
    print()
    C+=1
