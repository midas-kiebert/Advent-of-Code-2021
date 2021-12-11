# Parse the input, turn it into a list
moves = [move.split() for move in open('input.txt')]
depth = 0
depth2 = 0
horizontal = 0

for move in moves:
    if move[0] == 'down':
        depth += int(move[1])
    elif move[0] == 'up':
        depth -= int(move[1])
    else:
        depth2 += depth * (int(move[1]))
        horizontal += int(move[1])

print(depth * horizontal)
print(depth2 * horizontal)