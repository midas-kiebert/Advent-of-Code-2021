#!/bin/bash

YEAR="2021"

curl --silent -b $AOCSESSION https://adventofcode.com/$YEAR/day/$1/input -o ../inputs/$DAY.txt

ZERO="0"
if [ $1 -ge 10 ]; then
    ZERO=""
fi

DAY=day$ZERO$1

FILE=$DAY.cpp
if test -f "$FILE"; then
    exit
fi

cp template.cpp $FILE
sed -i 's/dayXX/'$DAY'/g' $FILE

if grep -q $DAY "Makefile"; then
    exit
fi

echo -e "\n$DAY.out: $FILE\n\tg++ -o $DAY.out $FILE\n" >> Makefile
sed -i '1{s/$/ '$DAY'.out/}' Makefile