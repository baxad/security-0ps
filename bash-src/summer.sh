#!/bin/bash -
#
# $ cut -d' ' -f1,10 access.log | bash summer.sh | sort -k 2.1 -rno
#
# Description:
# Sum the total of field 2 values for each unique field 1
#
# Usage: ./summer.sh
# input format: <name> <number>
#
declare -A cnt # assoc. array
while read id count
do
let cnt[$id]+=$count
done
for id in "${!cnt[@]}"
do
printf "%-15s %8\n" "${id}" "${cnt[${id}]}"
done



