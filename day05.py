import re, numpy as np

board = np.zeros([1000, 1000])

# Parse input, turn every line into a list of 4 integers.
lines = [list(map(int, num)) for num in [re.split(r'\D+', line.strip()) for line in open('inputs/day05.txt')]]

# Split the lines into 3 lists, vertical, horizontal and diagonal
vertical = [line for line in lines if line[0] == line[2]]
horizontal = [line for line in lines if line[1] == line[3]]
diagonal = [line for line in lines if line not in vertical and line not in horizontal]

# Add 1 to every coordinate the line crosses
for x1, y1, _, y2 in vertical:
    for i in range(y1, y2 + np.sign(y2 - y1), np.sign(y2 - y1)):
        board[i][x1] += 1

for x1, y1, x2, _ in horizontal:
    for i in range(x1, x2 + np.sign(x2 - x1), np.sign(x2 - x1)):
        board[y1][i] += 1

print(np.count_nonzero(board >= 2))

# Uses range that is inclusive and unordered
for x1, y1, x2, y2 in diagonal:
    for i, j in enumerate(range(x1, x2 + np.sign(x2 - x1), np.sign(x2 - x1))):
        board[y1 + i * np.sign(y2 - y1)][j] += 1

print(np.count_nonzero(board >= 2))
