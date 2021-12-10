import itertools, numpy as np

# Parse the input, turn it into a list
moves = [move.split() for move in open('input.txt')]
depth = 0
horizontal = 0

for move in moves:
    if move[0] == 'down':
        depth += int(move[1])
    elif move[0] == 'up':
        depth -= int(move[1])
    else:
        horizontal += int(move[1])

print(depth * horizontal)

aim = 0
depth = 0
for move in moves:
    if move[0] == 'down':
        aim += int(move[1])
    elif move[0] == 'up':
        aim -= int(move[1])
    else:
        depth += int(move[1]) * aim

print(depth * horizontal)