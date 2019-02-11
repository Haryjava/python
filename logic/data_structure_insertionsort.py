#!/usr/bin/env python3.5
import time

start = time.time()

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

data = [56,8,88,1,4,3,17,20,3,87]

insertionsort(data)
print()
print('Jumlah data: \t\t', len(data))

end = time.time()
print('Speed: \t\t\t', (end-start))
