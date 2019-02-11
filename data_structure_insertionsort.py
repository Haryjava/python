#!/usr/bin/env python3.5

def insertionsort(alist):
    print('Keadaan awal: \t\t', end='')
    print(alist)
    for i in range(1, len(alist)):
        currentvalue = alist[i]
        print('menyisipkan nilai %d: \t' % currentvalue, end='')
        position = i
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = currentvalue
        print(alist)

data = [12,8,15,6,7,10,31,3,1]

insertionsort(data)
