#! /bin/bash

mkdir data

for temp in $(cut -d "," -f 3 trp_cage.csv | uniq | tail --lines=+2)
#for temp in 300.00
do
    QUERY='$3 == "'
    QUERY+=${temp}
    QUERY+='" || $3 == "temperature [k]" { print }'
    echo $temp
    awk -F ',' "${QUERY}" trp_cage.csv > ./data/trp_$temp.csv
done