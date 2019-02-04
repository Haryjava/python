#!/bin/bash

# Static input array
arr=(10 8 20 100 12 8765 341 9 10)
echo "array in original order"

echo ${arr[*]}

# Performing BubbleSort
for((i=0; i<9; i++))
do
	for((j=i; j<9-i-1; j++))
	do
		if ((${arr[j]} > ${arr[$((j+1))]}))
		then
			#swap
			temp=${arr[$j]}
			arr[$j]=${arr[$((j+1))]}
			arr[$((j+1))]=$temp
		fi
	done
done

echo "Array in sorted order :"
echo ${arr[*]}
