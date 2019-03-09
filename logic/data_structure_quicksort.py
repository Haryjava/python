#!/usr/bin/env python3.5

import time

# Python program for implementation of Quicksort Sort 

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 

start = time.time()

def partition(arr,low,high):
    i = ( low-1 )        # index of smaller element
    pivot = arr[high]    # pivot
    
    for j in range(low , high): 

        # If current element is smaller than or 
        # equal to pivot
        print('arr[j] & pivot & j = %d & %d & %d \t\t' % (arr[j],pivot,j), end='')
        print()
        if arr[j] <= pivot:
            
            # increment index of smaller element
            i = i+1
            print('cond.bf arr[i], arr[j] & i & j = %d & %d & %d & %d \t\t' % (arr[i],arr[j], i, j), end='')
            arr[i],arr[j] = arr[j],arr[i]
            print('cond.aft arr[i], arr[j] & i & j = %d & %d & %d & %d \t\t' % (arr[i],arr[j], i, j), end='')
            print()

    print('++++++++++++++++++++++++++++++++++++++++++++')
    print('before arr[i+1], before arr[high] = %d & %d \t\t' % (arr[i+1],arr[high]), end='')            
    arr[i+1],arr[high] = arr[high],arr[i+1]
    print('after arr[i+1], after arr[high] = %d & %d \t\t' % (arr[i+1],arr[high]), end='')
    return ( i+1 ) 

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quickSort(arr,low,high):
    print()
    print('kondisi array terkini : ' , arr)
    print('low & high : %d & %d \t' % (low,high), end='')
    print()
    if low < high:
    
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high) 

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

# Driver code to test above 
arr = [56,8,88,1,4,3,17,20,3,87]
print('Initiate array : ', arr)
n = len(arr)
quickSort(arr,0,n-1) 

print ("Sorted array is:")
for i in range(n):
    print ("%d " % arr[i], end='')

print()
print()
end = time.time()
print('Speed time : ',(end-start))

# This code is contributed by Mohit Kumra
