import itertools, numpy as np

# Parse the input, turn it into a list
moves = [move.split() for move in open('input.txt')]

# Return an array of integers corresponding to the moves of direction
def movement(direction):
    return [int(move[1]) * (move[0] == direction) for move in moves]

# Make cumulative arrays for every down and up and a regular list for forward
down = np.array(list(itertools.accumulate(movement('down'))))
up = np.array(list(itertools.accumulate(movement('up'))))
forward = movement('forward')

aim = down - up
depth = sum(aim * forward)

print(aim[-1] * sum(forward))
print(depth * sum(forward))