import numpy as np

# Parse the input, make an array of initial positions
pos = np.array([int(x) for x in open('input.txt').read().split(',')])

# Try every number from the lowest to the highest position, the score is the sum of the
# differences of every position and that number. The lowest of these scores is the answer.
print(min([sum(abs(pos - i)) for i in range(min(pos), max(pos) + 1)]))

# 1 + 2 + ... + n = n(n + 1) / 2
print(min([sum((pos - i ) * (pos - i + 1) // 2) for i in range(min(pos), max(pos) + 1)]))
