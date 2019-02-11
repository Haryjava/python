#!/usr/bin/env python3.5

def bubblesort(alist):
    print('Keadaan awal: \t', alist)
    print()
    for i in range(0, len(alist)-1):
        print('Langkah ke-%d: \t' % (i+1), end='')
        for j in range(len(alist)-1, i, -1):
            if alist[j] < alist[j-1]:
                temp = alist[j]
                alist[j] = alist[j-1]
                alist[j-1] = temp
        print(alist)
    print()

data = [56,8,88,1,4,3,17,20,3,87]

# After
bubblesort(data)
print('Hasil akhir: \t', data)
# Count Data
print('Jumlah Data: \t',len(data))
