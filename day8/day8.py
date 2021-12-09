# Print the length of the list that contains every space separated string after a '|' of length 2, 3, 4 or 7.
print(len([word for word in ' '.join([line.strip().split(" | ")[1] for line in open('input.txt')]).split(' ') if len(word) == 2 or len(word) == 3 or len(word) == 4 or len(word) == 7]))

# Create a list of the input before the '|' and after the '|'. Every word is turned into a set of characters
lines = [[set(word) for word in (line.strip().split(" | ")[0].split())] for line in open('input.txt')]
displays = [[set(word) for word in (line.strip().split(" | ")[1].split())] for line in open('input.txt')]
total = 0

# For every line, create ten empty sets, which correspond to the digits.
# These sets will contain the letters that correspond to the digits that is the index of that set
# 1, 4, 7, 8 can easily be found, because of their unique amount of segments
#
# Remove 1, 4, 7, 8 from the potential candidate numbers for the remaining sets
#
# 9 is the only number with 6 segments which is a superset of 4
# After 9, 0 is the only number with 6 segments which is a superset of 1
# After 9 and 0, 6 is the only number with 6 segments
# 3 is the only number with 5 segments which is a superset of 1
#
# Remove 9, 0, 6, 8 from the potential candidates for the remaining sets
#
# Now the remaining 2 sets correspond to 5 and 2
# 5 is the only remaining number that is a subset of 6
# After 5, 2 is the only remaining number
#
# Now that every set has been placed into its correct index, add the number to the total
for i, line in enumerate(lines):
    sets = [{}] * 10
    for word in line:
        if len(word) == 2:
            sets[1] = word
        elif len(word) == 3:
            sets[7] = word
        elif len(word) == 4:
            sets[4] = word
        elif len(word) == 7:
            sets[8] = word
    line.remove(sets[1])
    line.remove(sets[4])
    line.remove(sets[7])
    line.remove(sets[8])
    for word in line:
        if len(word) == 6 and word & sets[4] == sets[4]:
            sets[9] = word
        elif len(word) == 6 and word & sets[1] == sets[1]:
            sets[0] = word
        elif len(word) == 5 and word & sets[1] == sets[1]:
            sets[3] = word
        elif len(word) == 6:
            sets[6] = word
    line.remove(sets[0])
    line.remove(sets[3])
    line.remove(sets[6])
    line.remove(sets[9])
    for word in line:
        if word & sets[6] == word:
            sets[5] = word
        else:
            sets[2] = word
    total += 1000 * sets.index(displays[i][0]) + 100 * sets.index(displays[i][1]) + 10 * sets.index(displays[i][2]) + sets.index(displays[i][3])

print(total)
