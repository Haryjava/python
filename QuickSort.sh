#!/bin/bash
PS4=':$LINENO+'; set -x

data=()
size=10
steps=0

for ((i=0; i<size; i++)); do
	    data[$i]=$((RANDOM % size))
    done

    partition() {
	        local pivot left right dest temp
		    pivot=${data[$1]}
		        left=$(($1 + 1))
			    right=$2
			        dest=$3

				    while true; do
					            while (( left <= right )) && (( ${data[$left]} <= pivot )); do
							                left=$(( left + 1 ))
									            steps=$(( steps + 1 ))
										            done

											            while (( right >= left )) && (( ${data[$right]} >= pivot )); do
													                right=$(( right - 1 ))
															            steps=$(( steps + 1 ))
																            done

																	            (( left > right )) && break

																		            temp=${data[$left]}
																			            data[$left]=${data[$right]}
																				            data[$right]=$temp
																					        done

																						    : '$1='"$1" right="$right" 'data[$1]='"${data[$1]}" 'data[$right]='"${data[$right]}"
																						        temp=${data[$1]}
																							    data[$1]=${data[$right]}
																							        data[$right]=$temp

																								    printf -v "$dest" %s "$right"
																							    }

																							    quickSort() {
																								        local partitionPoint
																									    if (( $1 < $2 )); then
																										            partition "$1" "$2" partitionPoint
																											            quickSort "$1" "$(( partitionPoint - 1 ))"
																												            quickSort "$((partitionPoint + 1))" "$2"
																													        fi
																													}

																													# involve the algorithm
																													quickSort 0 "$(( size - 1 ))"

																													echo "Steps: $steps"
																													printf '%s\n' "${data[@]}"
