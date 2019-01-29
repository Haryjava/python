#!/usr/bin/env python3.5

def bubblesort(alist):
    for i in range(0, len(alist)-1):
        for j in range(len(alist)-1, i, -1):
            if alist[j] < alist[j-1]:
                temp = alist[j]
                alist[j] = alist[j-1]
                alist[j-1] = temp


data = [9,7,8,5,1,9,3,5]

# Before
print(data)

# After
bubblesort(data)
print(data)
