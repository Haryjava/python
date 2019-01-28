#!/usr/bin/env python3.5
# Logic exercise
# Iniriate by HarysMatta - tifosilinux.wordpress.com


BARIS = 5
i = 1
while i <= BARIS:
        j = 1
        for x in range(1, BARIS):
            print("+ ", end='')

        for l in range(i, 1, -1):
            print('%d ' % (l*i),end='')

        #while l<=i:
        #    print('%d ' % (i*l), end='')
        #    l+=1

        while j<=i:
            print('%d ' % (i*j), end='')
            j+=1
            
        print() # new line
        i+=1
        BARIS-=1
print('\b')

BARU = 1
k = 5
while k >= BARU:
        l = 2
        while l <= k:
            print('+ ', end='')
            l += 1
        print() # new line
        k-=1
print("\b")

BARUU = 5
m = 1
while m <= BARUU:
    for n in range(2, m+1):
        print('%d ' % (m*n), end='')
    print() # new line
    m+=1

print()

##################################################################
##################################################################

BARIS = 5
KOLOM = 3
d = 1
while d <= BARIS:
    for f in range(1, KOLOM+1):
        print('%d %d | ' % (d,f), end='')
    print() # new line
    d+=1


print()

#### FINAL RESULT

BOUNDARIES = 5
A = 1
while A <= BOUNDARIES:
    for B in range(A, 1, -1):
        print('A = %d B %d' % (A,B), end='')
    print()
    A+=1

