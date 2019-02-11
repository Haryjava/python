#!/bin/bash

function insertionsort{
	echo "Keadaan awal : ";
	echo $alist;
	for i in $(seq 1 len(alist));
	do
		currentvalue = alist[$i]
		print("Menyisipkan nilai %d : " % currentvalue);
		position=$i
		while($position > 0 && alist[$position-1] > $currentvalue);
		do
			alist[$position] = alist[$position-1]
			$position--
		done
		alist[$position] = $currentvalue
		echo $alist;
	done
}
