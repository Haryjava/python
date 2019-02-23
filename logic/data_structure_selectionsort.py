#!/usr/bin/env python3.5
import time

start = time.time()

def selectionsort(alist):
    print('Keadaan awal: \t', alist)
    for i in range(0, len(alist)-1):
        print('Langkah ke-%d: \t' % (i+1), end='')
        minposition = len(alist)-1
        for j in range(len(alist)-2, i-1, -1):
            print('%d-%d : ' % (alist[j],alist[minposition]), end='')
            if alist[j] < alist[minposition]:
                minposition = j
        temp = alist[i]
        alist[i] = alist[minposition]
        alist[minposition] = temp
        print(alist)

data = [56,8,88,1,4,3,17,20,3,87]

selectionsort(data)
print()
print('Jumlah data: \t', len(data))

end = time.time()
print('Speed: \t\t',(end-start))
