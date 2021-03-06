# Parse input, save coords as set of tuples
# save instructions as a list of tuples containing the axis and where to fold
raw = open('inputs/day13.txt').read().split('\n\n')
coords = raw[0]
coords = set([tuple(int(x) for x in coord.split(',')) for coord in coords.split('\n')])
instructions = [tuple(line.split('g ')[1].split('=')) for line in raw[1].split('\n')]

#fold coords along the fold_line and axis
def fold(coords, fold_line, axis):
    to_be_folded = set([])
    after_fold = set([])
    for c in coords:
        # Add every point that will be folded to a set
        if c[axis] >= fold_line:
            to_be_folded.add(c)
        # Add the new coordinates after the fold to a set
        if c[axis] > fold_line:
            new = fold_line - (c[axis] - fold_line)
            if axis:
                after_fold.add((c[0], new))
            else:
                after_fold.add((new, c[1]))
    # Remove the coordinates to be folded and add the new coordinates
    coords -= to_be_folded
    coords |= after_fold

# Print amount of points after 1 instruction
fold(coords, int(instructions[0][1]), instructions[0][0] == 'y')
print(len(coords))

# Do the rest of the instructions
for instruction in instructions[1:]:
    fold(coords, int(instruction[1]), instruction[0] == 'y')

xmax = max(coord[0] for coord in coords)
ymax = max(coord[1] for coord in coords)

# Plot the result
for y in range(ymax + 1):
    line = ""
    for x in range(xmax + 1):
        if (x, y) in coords:
            line += "#"
        else:
            line += " "
    print(line)