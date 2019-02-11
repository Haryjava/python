#!/usr/bin/env python3.5

def selectionsort(alist):
    for i in range(0, len(alist)-1):
        print('Keadaan awal: \t\t', end='')
        print(alist)
        minposition = len(alist)-1
        for j in range(len(alist)-2, i-1, -1):
            if alist[j] < alist[minposition]:
                minposition = j
        temp = alist[i]
        alist[i] = alist[minposition]
        alist[minposition] = temp

data = [56,8,88,1,4,3,17,20,3,87]

selectionsort(data)
print()
print('Jumlah data: \t\t', len(data))
