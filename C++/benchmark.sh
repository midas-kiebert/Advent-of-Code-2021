FILE=results.txt
echo -e "C++:\n" > "$FILE"

for i in {01..25}
do
    DAY=day$i

    if [ ! -f "$DAY.out" ]; then
        break
    fi

    RESULT=$(./$DAY.out)
    echo "$DAY:" >> "$FILE"
    echo -e "$RESULT\n" >> "$FILE"
done