#!/bin/bash

YEAR="2021"

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

curl --silent -b $AOCSESSION https://adventofcode.com/$YEAR/day/$1/input -o ../inputs/$DAY.txt

if grep -q $DAY "Makefile"; then
    exit
fi

echo -e "\n$DAY: $FILE\n\tg++ -o $DAY $FILE\n" >> Makefile
sed -i '1{s/$/ '$DAY'/}' Makefile