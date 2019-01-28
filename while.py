#!/usr/bin/env python3.5
# Logic exercise
# Iniriate by HarysMatta - tifosilinux.wordpress.com


BARIS = 5
i = 1
while i <= BARIS:
        j = 1
        l = 2
        for x in range(1, BARIS):
            print("+ ", end='')

        while l<=i:
            print('%d ' % (i*l), end='')
            l+=1

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

LIMIT = 5
a = 1
while a <= LIMIT:
    for b in range(2, a+1):
        if a == 2:
            print('%d ' % (a*b), end='')
        else:
            print('%d ' % (a*b), end='')
    print()
    a+=1

print()


#### FINAL RESULT

limit = 5
A = 1
B = 5
while A <= limit:
    while B >= A:
        print('%d ' % (A*B), end='')
        B-=1
    print()
    A+=1
