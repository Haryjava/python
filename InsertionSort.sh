#!/bin/bash

echo "enter the number"
read n
echo "enter number in an array"

for((i=0;i<n;i++))
do
	read arr[$i]
done

#logic for insertion sort
for((i=1;i<n;i++))
do
	j=$i-1
	temp=${arr[$i]}
	while((j>=0 && arr[j]>temp))
	do
		arr[$j+1]=${arr[$j]}
		j=$j-1
	done
	arr[j+1]=$temp
done

#printing sorted array
echo "printing sorted array"
for((i=0;i<n;i++))
do
	echo ${arr[$i]}
done
