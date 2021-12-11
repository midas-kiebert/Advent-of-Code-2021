import numpy as np

OFFSETS = {(1,0), (0,1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)}
grid = np.array([[int(num) for num in line.strip()] for line in open('input.txt')])

def get_adj(x_coord, y_coord):
    adj = []
    for x, y in [(x_coord + dx, y_coord + dy) for dx, dy in OFFSETS]:
        if 0 <= x < 10 and 0 <= y < 10:
            adj.append((x, y))
    return adj

flash_count = 0
for i in range(1, 1000):
    grid += 1
    while (np.any(grid > 9)):
        flashed = [(x, y) for x in range(10) for y in range(10) if grid[x][y] > 9]
        for x, y in flashed:
            grid[x][y] = 0
            flash_count += 1
        for x, y in flashed:
            for x2, y2 in get_adj(x, y):
                 if grid[x2, y2] > 0:
                     grid[x2, y2] += 1
    if i == 100:
        print(flash_count)
    if not np.any(grid):
        print(i)
        break